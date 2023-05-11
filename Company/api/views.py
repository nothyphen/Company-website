from django.shortcuts import render
from rest_framework import generics
from blog.models import Article
from .serializers import ArticlesSerializers, UserSerializer
from django.contrib.auth.models import User
# Create your views here.

class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializers

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializers

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer