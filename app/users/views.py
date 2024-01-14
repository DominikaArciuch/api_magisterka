from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializers import CustomUserSerializer
from .swager_shemas import get_list_of_users


class UserFilterView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = CustomUser.objects.all().exclude(is_staff=True)
        username = self.request.GET.get("username")
        if username is not None:
            queryset = queryset.filter(username__startswith=username)
        return queryset

    @swagger_auto_schema(**get_list_of_users)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
