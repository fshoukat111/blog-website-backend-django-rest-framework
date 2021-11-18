from django.contrib import admin
from tinymce.widgets import TinyMCE
from blog_app.models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Categories, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {models.TextField: {'widget': TinyMCE()}}
admin.site.register(Posts, PostAdmin)
