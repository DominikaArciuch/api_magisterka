from rest_framework import serializers
from .models import Task
from users.models import CustomUser

from houses.models import House

from houses.serializers import HouseSerializer
from users.serializers import CustomUserSerializer


class TaskSerializer(serializers.ModelSerializer):
    assigned_users = CustomUserSerializer(many=True)
    house = HouseSerializer()
    class Meta:
        model = Task
        exclude = ['is_base']
        read_only_fields = ['id', 'house', 'created_by']

class CreateTaskSerializer(serializers.ModelSerializer):
    assigned_users = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all(), required=False)
    house = serializers.PrimaryKeyRelatedField(queryset=House.objects.all(), required=False)
    hardness = serializers.ChoiceField(choices=Task.VALUE_CHOICES)
    
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'hardness', 'assigned_users', 'house']

class BaseTaskSerializer(serializers.ModelSerializer):
    hardness = serializers.ChoiceField(choices=Task.VALUE_CHOICES)
    class Meta:
        model = Task
        fields = ['name', 'description', 'hardness']
        read_only_fields = ['id']


