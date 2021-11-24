from django.contrib import admin
from django import forms
from blog_app.models import *


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Categories, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug")
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Posts, PostAdmin)

