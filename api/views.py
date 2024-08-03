from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from django.urls import reverse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, authentication, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

# imports
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from . import models, serializers


class ProductView(generics.RetrieveAPIView):
    """
    return result trip search
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


# class OrderCreateView(generics.CreateAPIView):
#     serializer_class = serializers.OrderCreateSerializer


class OrderDetailView(generics.RetrieveAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderResponseSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderCreateView(generics.CreateAPIView):
    serializer_class = serializers.OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = models.Order.objects.create(
            lat=serializer.validated_data['lat'],
            lon=serializer.validated_data['lon'],
            eta=serializer.validated_data['eta'],
            payment_method=serializer.validated_data['payment_method']
        )

        order_items = serializer.validated_data['items']
        print(order_items)
        order_items_objects = [models.OrderItem(**item) for item in order_items]
        items = models.OrderItem.objects.bulk_create(order_items_objects)
        print(items)
        # order.items.add(items)

        return Response(serializer.data, status=status.HTTP_201_CREATED)