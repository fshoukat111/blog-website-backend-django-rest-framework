from django.contrib import admin
from django import forms
from apps.blog_articles.models import *


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug")
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Articles, ArticleAdmin)

