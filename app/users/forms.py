from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "first_name", "last_name")

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser

