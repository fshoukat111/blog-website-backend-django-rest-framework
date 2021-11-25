from django.conf.urls import include
from django.urls import path;
from rest_framework import routers
from blog_app.views import *

urlpatterns = [
    path('categories', CategorysList.as_view()),
    path('post/<slug:category_slug>', PostsList.as_view()),
    path('post/<slug:category_slug>/<slug:post_slug>', PostDetail.as_view()),
    path("post/<slug:post_slug>/comment/create/",CreateComments.as_view()),
]