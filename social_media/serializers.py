from rest_framework import serializers

from user.serializers import UserSerializer
from .models import Post, Profile


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "content",
            "image",
            "created_at",
            "updated_at",
            "hashtag"
        )
        read_only_fields = ("created_at", "updated_at")


class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "created_at",
            "updated_at",
            "user",
            "hashtags"
        )


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    followers = UserSerializer(many=True, read_only=True)
    follow = serializers.BooleanField(read_only=False)

    class Meta:
        model = Profile
        fields = ("id", "user", "profile_pic", "bio", "followers", "follow")
        read_only_fields = ("id", "user", "followers")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = self.context["request"].user
        data["follow"] = user in instance.followers.all()
        return data

    def update(self, instance, validated_data):
        follow = validated_data.pop("follow", None)
        if follow is not None:
            user = self.context.get("request").user
            if follow:
                instance.followers.add(user)
            else:
                instance.followers.remove(user)

        return super().update(instance, validated_data)



class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Profile
        fields = ("id", "user", "profile_pic", "bio",)
