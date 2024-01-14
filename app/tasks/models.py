from django.db import models
from users.models import CustomUser

from houses.models import House


class Task(models.Model):
    VALUE_CHOICES = [(i, str(i)) for i in range(1, 11)]
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    hardness = models.IntegerField(choices=VALUE_CHOICES, null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_tasks')
    assigned_users = models.ManyToManyField(CustomUser, related_name='assigned_tasks', blank=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    is_done = models.BooleanField(default=False)
    is_base = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.name
