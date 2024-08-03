from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    # product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['quantity', 'product']


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['items', 'lat', 'lon', 'eta', 'payment_method']


class OrderResponseSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    item = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'lat', 'lon', 'eta', 'date', 'payment_method', 'item']

    @extend_schema_field(str)
    def get_date(self, obj):
        return obj.created_at.strftime('%d %B, %Y')
