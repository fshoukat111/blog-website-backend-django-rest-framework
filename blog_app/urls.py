from django.conf.urls import include
from django.urls import path;
from rest_framework import routers
from blog_app.views import *

urlpatterns = [
    path('post/<slug:category_slug>', PostsList.as_view()),
    path('categories', CategorysList.as_view()),
]