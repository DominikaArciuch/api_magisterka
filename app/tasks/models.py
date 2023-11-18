from django.db import models


class Task(models.Model):
    VALUE_CHOICES = [(i, str(i)) for i in range(1, 11)]
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    hardness = models.IntegerField(choices=VALUE_CHOICES)
    is_done = models.BooleanField(default=False)


    def __str__(self):
        return self.name
