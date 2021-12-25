
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http.response import Http404
from rest_framework.pagination import PageNumberPagination

from apps.blog_articles.models import *
from apps.blog_categories.models import *
from apps.blog_articles.serializers import *


# Create your views here.
class ArticlesListView(APIView):

    def get(self, request, category_slug):
        category = get_object_or_404(Categories, slug=category_slug)
        articles_list = Articles.objects.filter(category=category)
        paginator = PageNumberPagination()
        page_article_list = paginator.paginate_queryset(
            articles_list, request, view=self)
        serializer = ArticlesSerializer(page_article_list, many=True)
        return Response(serializer.data)

#Get Single Article Detail
class ArticleDetailView(APIView):

    def get_object(self, category_slug, article_slug):
        category_list = get_object_or_404(Categories, slug=category_slug)
        try:
            return Articles.objects.filter(category=category_list).get(slug=article_slug)
        except Articles.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, article_slug):
        article_detail = self.get_object(category_slug, article_slug)
        serializer = ArticlesSerializer(article_detail)
        return Response(serializer.data)


