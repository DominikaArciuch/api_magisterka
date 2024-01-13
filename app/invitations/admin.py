from django.contrib import admin

from .models import Invitation

class InvitationAdmin(admin.ModelAdmin):
    list_display = ("user", "house", "is_used")

admin.site.register(Invitation, InvitationAdmin)
