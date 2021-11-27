from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from apps.blog_post.models import *
from apps.blog_comment.models import *
from apps.blog_comment.serializers import *

# Create your views here.
class CreateComments(APIView):
    serializer_class = CommentSerializer

    def post(self, request, post_slug, *args, **kwargs):
        post = get_object_or_404(Posts, slug=post_slug)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(comments_on_post=post)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)

class CommentsList(APIView):
    serializer_class = CommentSerializer

    def get(self, request,post_slug):
        post_list = get_object_or_404(Posts, slug=post_slug)
        comment_of_posts = Comments.objects.filter(comments_on_post=post_list)
        serializer = CommentSerializer(comment_of_posts,many=True)
        return Response(serializer.data)

