from drf_yasg import openapi
from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers
from .models import House
from users.serializers import CustomUserSerializer

from users.models import CustomUser

from users.serializers import CustomUserForHouseSerializer


class HouseSerializer(serializers.ModelSerializer):
    users = CustomUserSerializer(many=True, read_only=True)
    house_owner = CustomUserSerializer(read_only=True)

    class Meta:
        model = House
        fields = "__all__"
        read_only_fields = ['id']


class ListHousesSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    users = serializers.SerializerMethodField()

    class Meta:
        model = House
        fields = ['id', 'name', 'description', 'users', 'role']

    def get_role(self, obj):
        if obj.house_owner == self.context['request'].user:
            return "admin"
        else:
            return "user"

    def get_users(self, obj):
        return [user.username for user in obj.users.all()]




class UpdateHouseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    color = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all(), required=False)

    class Meta:
        model = House
        fields = ['name', 'color', 'description', 'users']


class CreateHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['name', 'color', 'description']


class BasicHouseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'name', 'description']
