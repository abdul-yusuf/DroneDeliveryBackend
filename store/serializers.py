from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import *
from store.models import *
from order.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ('pk', 'name', 'price', 'category', 'vendor', 'weight', 'unit', 'description', 'image')

    # def pk