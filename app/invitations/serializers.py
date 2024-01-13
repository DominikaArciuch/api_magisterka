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
        read_only_fields = ['id']

class BasicInvitationSerializer(serializers.ModelSerializer):
    house = BasicHouseInfoSerializer()
    class Meta:
        model = Invitation
        fields = ['id', 'house']

class InvitationSerializer(serializers.ModelSerializer):
    house = HouseSerializer()
    class Meta:
        model = Invitation
        fields = ['id', 'house']

class InvitationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ['is_accepted']

