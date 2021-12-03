from django.contrib import admin
from apps.blog_categories.models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Categories, CategoryAdmin)
