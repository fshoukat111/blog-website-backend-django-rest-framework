from typing import DefaultDict
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from blog_app.serializers import *
from blog_app.models import *

# Create your views here.


class CategorysList(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        category_list = Categories.objects.all()
        serializer = CategoriesSerializer(category_list, many=True)
        return Response(serializer.data)


class PostsList(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request,category_slug):
        category_list = get_object_or_404(Categories, slug=category_slug)
        posts_list = Posts.objects.filter(category=category_list)
        serializer = PostsSerializer(posts_list, many=True)
        return Response(serializer.data)

