# Generated by Django 4.0.4 on 2023-04-21 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("social_media", "0010_profile_follow"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="follow",
            field=models.BooleanField(default=None),
        ),
    ]