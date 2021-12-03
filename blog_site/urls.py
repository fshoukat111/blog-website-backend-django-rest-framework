from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.blog_categories.urls')),
    path('api/', include('apps.blog_articles.urls')),
    path('api/', include('apps.blog_article_comments.urls')),
]
