# Generated by Django 4.0.4 on 2023-04-21 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("social_media", "0005_profile_followers"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="followers",
            new_name="followed",
        ),
    ]
