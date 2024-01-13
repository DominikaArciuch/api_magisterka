from django.db import models
import uuid
from users.models import CustomUser
from houses.models import House

class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_invitation')
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_invitation')
    is_used = models.BooleanField(default=False)
    is_accepted = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} for house {self.house}"
