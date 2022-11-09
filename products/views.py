from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.models import ProductCategory
from products.serializers import ProductCategorySerializer
# Create your views here.

class ProductCategoryListView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
