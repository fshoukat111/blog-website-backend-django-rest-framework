from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from rest_framework import pagination

from apps.blog_articles.models import *
from apps.blog_categories.serializers import *
from apps.blog_article_comments.serializers import *

class ArticlesSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer(read_only=True,many=True)
    comments = CommentSerializer(read_only=True)
    
    class Meta:
        model = Articles
        fields = [
            'id', 
            'title',
            'slug',
            'post_image',
            'body_content',
            'created',
            'category',
            'comments',
        ]

