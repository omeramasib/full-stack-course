from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.models import ProductCategory, Maker, Product
from products.serializers import ProductCategorySerializer, MakerSerializer, ProductSerializer
# Create your views here.

class ProductCategoryListView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class MakerListView(ListAPIView):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer

class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
