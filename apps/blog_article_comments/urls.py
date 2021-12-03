from django.urls import path
from apps.blog_article_comments.views import *

urlpatterns = [
    path("article/<slug:article_slug>/comment/list",CommentsView.as_view()),
]
