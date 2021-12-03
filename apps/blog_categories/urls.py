from django.urls import path;
from apps.blog_categories.views import *

urlpatterns = [
    path('categories', CategoriesList.as_view()),
    
]