from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        email,
        password,
        first_name,
        last_name,
        phone,
        company=None,
        is_active=False,
        is_staff=False,
        **extra_fields
    ):
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            company=company,
            is_active=is_active,
            is_staff=is_staff,
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("first_name", "admin")
        extra_fields.setdefault("last_name", "admin")
        extra_fields.setdefault("phone", "")
        extra_fields.setdefault("company", None)

        return self.create_user(email, password, is_active=True, **extra_fields)
