from rest_framework import generics, status

from .models import House
from .serializers import HouseSerializer, HouseCreateSerializer


class HouseListCreateView(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseCreateSerializer

    def perform_create(self, serializer):
        serializer.save()


class HouseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer




