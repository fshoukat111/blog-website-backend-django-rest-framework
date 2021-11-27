from django.urls import path;
from apps.blog_comment.views import *

urlpatterns = [
    path("post/<slug:post_slug>/comment/create",CreateComments.as_view()),
    path("post/<slug:post_slug>/comment/list",CommentsList.as_view()),
]

