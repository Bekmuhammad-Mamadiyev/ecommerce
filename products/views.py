from django.shortcuts import render
from rest_framework.generics import ListAPIView

from products.models import Category, Product
from products.serializers import CategoryListSerializer, ProductListSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = None


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
