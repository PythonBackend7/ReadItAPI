from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView


# Create your views here.


class HomeView(ListAPIView):
    queryset = Post.objects.all().order_by('-id')[:2]
    serializer_class = PostSerializer


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class AuthorView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class Commentview(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        category = self.request.query_params.get('cat')
        q = self.request.query_params.get('q')

        if tag:
            return Post.objects.filter(tags__name=tag)
        if category:
            return Post.objects.filter(category__name=category)
        if q:
            return Post.objects.filter(title__icontains=q)

