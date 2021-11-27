
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http.response import Http404
from rest_framework.pagination import PageNumberPagination

from apps.blog_post.serializers import *
from apps.blog_post.models import *

# Create your views here.

# Get CategoriesList
class CategoriesList(APIView):

    def get(self, request):
        category_list = Categories.objects.all()
        serializer = CategoriesSerializer(category_list, many=True)
        return Response(serializer.data)

# Get PostsList based on Categories
class PostsList(APIView):

    def get(self, request, category_slug):
        category_list = get_object_or_404(Categories, slug=category_slug)
        posts_list = Posts.objects.filter(category=category_list)
        paginator = PageNumberPagination()
        pages_of_posts = paginator.paginate_queryset(
            posts_list, request, view=self)
        serializer = PostsSerializer(pages_of_posts, many=True)
        return Response(serializer.data)

#Get Single Post Detail
class PostDetail(APIView):

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


