from django.contrib.auth import get_user_model
from rest_framework import generics

from blog.api.serializers import PostSerializer, UserSerializer
from blog.models import Post
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

User = get_user_model()


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer
