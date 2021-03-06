from rest_framework import viewsets, filters

from core.models import Product
from product.serializers import ProductFullSerializer


class ProductListView(viewsets.ModelViewSet):
    queryset = Product.objects.filter(active=True).order_by('id')
    serializer_class = ProductFullSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']