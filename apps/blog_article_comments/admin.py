from django.contrib import admin

from apps.blog_article_comments.models import *

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','email','article_comments']

admin.site.register(Comments,CommentAdmin)
