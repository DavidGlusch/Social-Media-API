# Generated by Django 4.0.4 on 2023-04-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("social_media", "0004_post_hashtag"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="followers",
            field=models.ManyToManyField(related_name="following", to="social_media.profile"),
        ),
    ]