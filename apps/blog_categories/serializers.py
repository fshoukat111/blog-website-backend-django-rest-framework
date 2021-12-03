from rest_framework import serializers

from apps.blog_categories.models import *

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name','slug']



