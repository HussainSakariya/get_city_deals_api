from django.urls import path,include
from rest_framework import routers
from .views import *

route=routers.DefaultRouter()
route.register('categories',CategoriesViewset)
route.register('subcategories',SubCategoriesViewset)

urlpatterns = [
    path('', include(route.urls)),   
]