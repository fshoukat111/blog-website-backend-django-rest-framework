
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.http.response import Http404
from rest_framework.pagination import PageNumberPagination

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

    def get(self, request, category_slug):
        category_list = get_object_or_404(Categories, slug=category_slug)
        posts_list = Posts.objects.filter(category=category_list)
        paginator = PageNumberPagination()
        pages_of_posts = paginator.paginate_queryset(
            posts_list, request, view=self)
        serializer = PostsSerializer(pages_of_posts, many=True)
        return Response(serializer.data)


class PostDetail(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, category_slug, post_slug):
        category_list = get_object_or_404(Categories, slug=category_slug)
        try:
            return Posts.objects.filter(category=category_list).get(slug=post_slug)
        except Posts.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, post_slug):
        post_detail = self.get_object(category_slug, post_slug)
        serializer = PostsSerializer(post_detail)
        return Response(serializer.data)


class CreateComments(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer

    def post(self, request, post_slug, *args, **kwargs):
        post = get_object_or_404(Posts, slug=post_slug)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(comment_posts=post)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)
