# Generated by Django 4.2.1 on 2024-01-13 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_time_task_due_date_task_assigned_to_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='assigned_to_user',
            new_name='assigned_user',
        ),
    ]
