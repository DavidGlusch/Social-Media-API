# Generated by Django 4.0.4 on 2023-04-21 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("social_media", "0006_rename_followers_profile_followed"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="followed",
        ),
    ]
