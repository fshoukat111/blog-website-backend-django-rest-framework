from django.conf.urls import include
from django.urls import path;
from rest_framework import routers
from blog_app.views import *

urlpatterns = [
    path('post_list', PostsList.as_view()),
    path('posts/<slug:category_slug>', PostsListByCategory.as_view()),
    path('categories', CategorysList.as_view()),
]