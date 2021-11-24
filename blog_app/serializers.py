from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from rest_framework import pagination

from blog_app.models import *

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name','slug']

class PostsSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer(read_only=True,many=True)
    
    class Meta:
        model = Posts
        fields = ['id', 'title','slug','post_image', 'body_content', 'created','category']