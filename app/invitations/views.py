from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Invitation
from .serializers import InvitationSerializer, CreateInvitationSerializer, InvitationUpdateSerializer, \
    BasicInvitationSerializer
from .swagger_schemas import send_invitation_schema, get_invitation_schema, solve_invitation_schema, \
    get_invitations_list_schema


class SendInvitationView(generics.ListCreateAPIView):
    queryset = Invitation.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateInvitationSerializer
        return BasicInvitationSerializer

    @swagger_auto_schema(**send_invitation_schema)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print("strzal")
        if serializer.is_valid():
            is_user_already_invited = Invitation.objects.filter(user=serializer.validated_data['user'],
                                                                house=serializer.validated_data['house']).exists()
            if is_user_already_invited:
                return Response({"error": ["User is already invited to this house."]},
                                status=status.HTTP_400_BAD_REQUEST)
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Invitation.objects.all()
        user = self.request.user
        if user.is_superuser:
            return queryset
        else:
            queryset = queryset.filter(user=user, is_used=False)
        return queryset

    @swagger_auto_schema(**get_invitations_list_schema)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class InvitationView(generics.RetrieveUpdateAPIView):
    queryset = Invitation.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return InvitationUpdateSerializer
        return BasicInvitationSerializer

    @swagger_auto_schema(**get_invitation_schema)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(**solve_invitation_schema)
    def patch(self, request, *args, **kwargs):
        invitation = self.get_object()
        is_accepted = request.data.get('is_accepted')
        user = self.request.user
        if is_accepted is not None:
            invitation.is_used = True
            if is_accepted:
                house = invitation.house
                house.users.add(user)
                house.save()
                invitation.is_accepted = is_accepted
            invitation.save()
            return Response(InvitationSerializer(invitation).data, status=status.HTTP_200_OK)
        return Response({"is_accepted": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(method='put', auto_schema=None)
    @api_view(['PUT'])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
