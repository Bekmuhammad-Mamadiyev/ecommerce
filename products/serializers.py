from rest_framework import serializers
from products.models import Category, Product
from common.serializers import MediaSerializer


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('image',)


class ProductListSerializer(serializers.ModelSerializer):
    thumbnail = MediaSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category', 'in_stock', 'brand', 'discount', 'thumbnail')
