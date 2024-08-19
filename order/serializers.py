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
        fields = ['pk', 'lat', 'lon', 'eta', 'date', 'payment_method', 'item']

    @extend_schema_field(str)
    def get_date(self, obj):
        return obj.created_at.strftime('%d %B, %Y')


class OrderListSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    weight = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    item = OrderItemSerializer(many=True)

    # image: "assets/images/product1.jpg"
    # name: 'Cartier MD'
    # weight: '2.1kg'
    # unit: '2.1kg'
    # date: 'Jul 15,2024 - 10:45 AM'
    # price: '12000.00'

    class Meta:
        model = Order
        fields = ['pk', 'name', 'lat', 'lon', 'eta', 'date', 'price', 'payment_method', 'item', 'weight', 'status']

    @extend_schema_field(str)
    def get_date(self, obj):
        return obj.created_at.strftime('%d %B, %Y')

    @extend_schema_field(str)
    def get_price(self, obj):
        price = sum([item.product.price * item.quantity for item in obj.item.get_queryset().all()])

        return price

    @extend_schema_field(str)
    def get_name(self, obj):
        items_name = ''.join(item.product.name for item in obj.item.get_queryset().all())

        return items_name

    @extend_schema_field(str)
    def get_weight(self, objs):
        objs = objs.item.get_queryset().all()
        weight = []
        print(objs)
        for obj in objs:
            if obj.product.unit == 'kg':
                weight.append((obj.product.weight*1000)*obj.quantity)
            else:
                weight.append(obj.product.weight*obj.quantity)
        total = sum(weight)
        if total >= 1000:
            total = str(total)+' kg'
        else:
            total = str(total)+' gram'
        return total

    @extend_schema_field(str)
    def get_status(self, obj):
        return obj.status.upper()