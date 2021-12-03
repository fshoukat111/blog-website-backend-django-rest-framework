from django.urls import path;
from apps.blog_articles.views import *

urlpatterns = [
    path('article/<slug:category_slug>', ArticlesListView.as_view()),
    path('article/<slug:category_slug>/<slug:article_slug>',ArticleDetailView.as_view()),
    
]