import uuid

from django.db import models

from users.models import CustomUser


class House(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    users = models.ManyToManyField(CustomUser, related_name='houses')
    house_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='house_owner')

    def __str__(self):
        return self.name