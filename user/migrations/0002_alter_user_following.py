# Generated by Django 4.0.4 on 2023-04-21 18:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="following",
            field=models.ManyToManyField(related_name="users", to=settings.AUTH_USER_MODEL),
        ),
    ]
