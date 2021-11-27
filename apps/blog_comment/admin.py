from django.contrib import admin

from apps.blog_comment.models import *

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','email','comments_on_post']

admin.site.register(Comments,CommentAdmin)
