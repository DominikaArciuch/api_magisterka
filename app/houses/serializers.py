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

class UpdateHouseSerializer(serializers.ModelSerializer):
    name=serializers.CharField(required=False)
    color=serializers.CharField(required=False)
    description=serializers.CharField(required=False)
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all(), required=False)
    class Meta:
        model = House
        fields = ['name', 'color', 'description', 'users']

class BasicHouseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'name', 'description']


