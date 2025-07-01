from django.shortcuts import render
from rest_framework import viewsets
from .models import Category,Tag, Product
from .serializers import(
    CategorySerializer,TagSerializer,ProductSerializer,ProductHyperSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.select_related('category').prefetch_related('tags')
    def get_serializer_class(self):
        if self.request.query_params.get('view')=='hyper':
            return ProductHyperSerializer
        return ProductSerializer
