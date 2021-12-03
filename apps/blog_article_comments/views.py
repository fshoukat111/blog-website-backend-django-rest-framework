from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from apps.blog_articles.models import *
from apps.blog_article_comments.models import *
from apps.blog_article_comments.serializers import *

# Create your views here.
class CommentsView(APIView):
    serializer_class = CommentSerializer
    
    def get(self, request,article_slug):
        article = get_object_or_404(Articles, slug=article_slug)
        article_comments = Comments.objects.filter(article_comments=article)
        serializer = CommentSerializer(article_comments,many=True)
        return Response(serializer.data)

    def post(self, request, article_slug, *args, **kwargs):
        post = get_object_or_404(Articles, slug=article_slug)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article_comments=post)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)
