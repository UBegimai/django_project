from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets


from .filters import ProductFilter
from .models import Product

from .serializers import ProductListSerializer, ProductDetailsSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = ProductFilter
    ordering_fields = ['title', 'price']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return self.serializer_class
