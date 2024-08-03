from rest_framework import generics, authentication, permissions, viewsets
from . import models, serializers


class ProductView(generics.ListAPIView):
    """
    return result trip search
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


