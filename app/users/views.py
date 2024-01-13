from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer


class UserFilterView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        queryset = CustomUser.objects.all().exclude(is_staff=True)
        username = self.request.GET.get("username")
        if username is not None:
            queryset = queryset.filter(username__startswith=username)
        return queryset