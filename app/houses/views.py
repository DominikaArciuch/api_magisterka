from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import House
from .serializers import HouseSerializer, UpdateHouseSerializer, ListHousesSerializer, CreateHouseSerializer
from .swagger_schemas import get_house_schema, delete_house_schema, edit_house_schema, create_house_schema, \
    get_house_list_schema


class HouseListCreateView(generics.ListCreateAPIView):
    queryset = House.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateHouseSerializer
        return ListHousesSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return House.objects.all()
        else:
            return House.objects.filter(users=user)

    @swagger_auto_schema(**get_house_list_schema)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(**create_house_schema)
    def post(self, request, *args, **kwargs):
        print(request.data)
        data = self.get_serializer(data=request.data)
        if data.is_valid():
            data.save(house_owner=request.user)
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class HouseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HouseSerializer
    queryset = House.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return UpdateHouseSerializer
        return HouseSerializer

    @swagger_auto_schema(**get_house_schema)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(**edit_house_schema)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(**delete_house_schema)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(method='put', auto_schema=None)
    @api_view(['PUT'])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)




