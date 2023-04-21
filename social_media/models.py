from django.db import models

from social_media_api import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    profile_pic = models.ImageField(
        upload_to="profile_pics/",
        null=True,
        blank=True
    )
    bio = models.TextField(null=True, blank=True)
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="profiles",
        symmetrical=False,
        blank=True
    )
    follow = models.BooleanField(default=None)


    def __str__(self):
        return f"Profile of {self.user}"


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hashtag = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Post written by {self.user}"
