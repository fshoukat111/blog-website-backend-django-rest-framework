from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.blog_categories.models import *
from apps.blog_categories.serializers import *

# Create your views here.
# Get CategoriesList
class CategoriesList(APIView):
        
    def get(self, request):
        category_list = Categories.objects.all()
        serializer = CategoriesSerializer(category_list, many=True)
        return Response(serializer.data)
