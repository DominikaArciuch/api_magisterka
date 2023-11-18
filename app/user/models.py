from django.contrib.auth.models import AbstractUser
from django.db import models

from app.user.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30)
    password2 = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
