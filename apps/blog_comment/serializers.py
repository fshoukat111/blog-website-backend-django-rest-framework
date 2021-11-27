from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from apps.blog_comment.models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            "id",
            "comments_on_post",
            "full_name",
            "email",
            "comment_content",
            "created",
        ]