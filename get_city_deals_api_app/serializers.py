from rest_framework import serializers
from rest_framework import fields
from .models import *

class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields="__all__"

class SubCategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model=SubCategories
        fields="__all__"