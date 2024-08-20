from rest_framework import generics, authentication, permissions, viewsets
from . import models, serializers
from .models import UserNotification
from django.shortcuts import render

class ProductView(generics.ListAPIView):
    """
    return result trip search
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


def user_notifications(request):
    user = request.user
    notifications = UserNotification.objects.filter(user=user).select_related('notification')

    return render(request, 'notifications/user_notifications.html', {'notifications': notifications})