from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Post
from .serializers import PostSerializer,UserSerializer
from .permissions import IsAuthorOrReadOnly,IsCurrentUserOrAdmin
from django.contrib.auth import get_user_model

class PostList(generics.ListCreateAPIView): #has_object_permission not called for list views so we need to override has_permission
    permission_classes = (IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsCurrentUserOrAdmin,)
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer
# Create your views here.
