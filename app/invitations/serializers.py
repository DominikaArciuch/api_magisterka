from rest_framework.relations import PrimaryKeyRelatedField
from users.serializers import CustomUserSerializer
from rest_framework import serializers
from houses.serializers import BasicHouseInfoSerializer

from .models import Invitation
from houses.models import House
from users.models import CustomUser

from houses.serializers import HouseSerializer


class CreateInvitationSerializer(serializers.ModelSerializer):
    user = PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    house = PrimaryKeyRelatedField(queryset=House.objects.all())
    class Meta:
        model = Invitation
        fields = ['user', 'house']
        read_only_fields = ['id', 'is_used']

class BasicInvitationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    house = BasicHouseInfoSerializer()
    class Meta:
        model = Invitation
        fields = "__all__"

class InvitationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    house = HouseSerializer()
    class Meta:
        model = Invitation
        fields = "__all__"

class InvitationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ['is_accepted']

