# Generated by Django 3.0.5 on 2020-06-06 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_system_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='fcm_token',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='student',
            name='fcm_token',
            field=models.TextField(default=''),
        ),
    ]
