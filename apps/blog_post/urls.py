from django.urls import path;
from apps.blog_post.views import *

urlpatterns = [
    path('categories', CategoriesList.as_view()),
    path('post/<slug:category_slug>', PostsList.as_view()),
    path('post/<slug:category_slug>/<slug:post_slug>', PostDetail.as_view()),
    
]