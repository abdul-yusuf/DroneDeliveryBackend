from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    # product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.OrderItem
        fields = ['quantity', 'product']


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = models.Order
        fields = ['user', 'items', 'lat', 'lon', 'eta', 'payment_method']


class OrderResponseSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = models.Order
        fields = ['lat', 'lon', 'eta', 'date', 'payment_method']

    def get_date(self, obj):
        return obj.created_at.strftime('%d %B, %Y')
