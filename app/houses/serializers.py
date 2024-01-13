from rest_framework import serializers
from .models import House
from users.serializers import CustomUserSerializer

from users.models import CustomUser


class HouseSerializer(serializers.ModelSerializer):
    users = CustomUserSerializer(many=True, read_only=True)
    house_owner = CustomUserSerializer(read_only=True)
    class Meta:
        model = House
        fields = "__all__"

class BasicHouseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'name', 'description']

class HouseCreateSerializer(serializers.ModelSerializer):
    users = CustomUserSerializer(many=True, read_only=True)
    house_owner = CustomUserSerializer(read_only=True)
    class Meta:
        model = House
        fields = ['id', 'name', 'color', 'description', 'users', 'house_owner']

    def create(self, validated_data):
        user = self.context['request'].user
        user = CustomUser.objects.get(id=user.id)
        house = House.objects.create(**validated_data, house_owner=user)
        house.users.add(user)
        return house
