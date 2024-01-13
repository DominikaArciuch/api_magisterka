# Generated by Django 4.2.1 on 2024-01-13 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='house_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
