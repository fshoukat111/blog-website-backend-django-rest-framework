from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from apps.blog_article_comments.models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = (
            "id",
            "full_name",
            "email",
            "comment_content",
            "article_comments",
            "created",
        )