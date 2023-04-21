from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Profile
from .serializers import PostSerializer, ProfileSerializer, ProfileDetailSerializer

from rest_framework.permissions import BasePermission



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {"success": True}
        return response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related("user")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.action == "list":
            return Post.objects.all()
        elif self.action == "retrieve":
            return Post.objects.filter(pk=self.kwargs.get("pk"))
        return Post.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().select_related("user")
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProfileDetailSerializer
        return self.serializer_class

    def get_queryset(self):
        if self.action == "list":
            queryset = Profile.objects.all()
            search_query = self.request.query_params.get("search", None)
            if search_query:
                queryset = queryset.filter(
                    Q(user__email__icontains=search_query)
                )
            return queryset
        elif self.action == "retrieve":
            return Profile.objects.filter(pk=self.kwargs.get("pk"))
        return Profile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        follow = self.request.data.get("follow", None)
        if follow is not None and (self.request.method == "PATCH" or self.request.method == "PUT"):
            instance = serializer.instance
            user = self.request.user
            if follow:
                instance.followers.add(user)
            else:
                instance.followers.remove(user)
        serializer.save()
