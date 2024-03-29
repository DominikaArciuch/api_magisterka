# Generated by Django 4.2.1 on 2024-01-15 21:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_used', models.BooleanField(default=False)),
                ('is_accepted', models.BooleanField(blank=True, null=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house_invitation', to='houses.house')),
            ],
        ),
    ]
