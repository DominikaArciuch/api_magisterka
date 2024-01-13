from django.contrib import admin

from .models import House


class HouseAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(House, HouseAdmin)
