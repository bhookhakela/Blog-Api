from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
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
# Create your views here.
