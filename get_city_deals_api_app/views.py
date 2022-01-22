from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets

class CategoriesViewset(viewsets.ModelViewSet):
    serializer_class=CategoriesSerializers
    queryset=Categories.objects.all()

class SubCategoriesViewset(viewsets.ModelViewSet):
    serializer_class=SubCategoriesSerializers
    queryset=SubCategories.objects.all()