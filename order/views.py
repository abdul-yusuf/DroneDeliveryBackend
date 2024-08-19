from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from . import models, serializers
from order.models import Order, OrderItem


# Create your views here.

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderResponseSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderListView(generics.ListAPIView):
    # queryset = Order.objects.all()
    serializer_class = serializers.OrderListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the objects for the currently
        authenticated user.
        """
        user = self.request.user
        return Order.objects.filter(user=user).order_by("-created_at")


class OrderCreateView(generics.CreateAPIView):
    serializer_class = serializers.OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = Order.objects.create(
            user=request.user,
            lat=serializer.validated_data['lat'],
            lon=serializer.validated_data['lon'],
            eta=serializer.validated_data['eta'],
            payment_method=serializer.validated_data['payment_method']
        )
        order.save()
        print(serializer.data)

        for item_data in serializer.validated_data.pop('items'):
            OrderItem.objects.create(order=order, **item_data)
        # serializer.validated_data
        print(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
