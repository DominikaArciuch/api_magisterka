from rest_framework import serializers

from app.user.models import CustomUser


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"