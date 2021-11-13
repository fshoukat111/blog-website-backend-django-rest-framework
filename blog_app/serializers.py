from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from blog_app.models import *

class CategoriesSerializer(serializers.ModelSerializer):
    # posts = PostsSerializer(many=True,read_only=True)
    class Meta:
        model = Categories
        fields = ('id', 'name','slug')


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'title','slug', 'body_content', 'created')

class PostsByCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'title','slug', 'body_content', 'created','category')