from rest_framework import generics,filters
from .models import Product
from .serializers import ProductSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from .filters import ProductFilter

#filter by current user

class ProductListByUser(generics.ListCreateAPIView):
    serializer_class=ProductSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Product.objects.filter(owner=self.request.user)
        return Product.objects.none()

    def perform_create(self, serializer):
        queryset = Product.objects.filter(owner=self.request.user)
        if queryset.exists():
            raise ValidationError('You have already signed up')  # Optional logic
        serializer.save(owner=self.request.user)


class ProductListByURL(generics.ListAPIView):
    serializer_class=ProductSerializer

    def get_queryset(self):
        username=self.kwargs['username']
        return Product.objects.filter(owner__username=username)

class ProductListQueryParam(generics.ListAPIView):
    serializer_class=ProductSerializer
    def get_queryset(self):
        queryset=Product.objects.all()
        username=self.request.query_params.get('username')
        if username:
            queryset=queryset.filter(owner__username=username)
        return queryset
    
class ProductListFilterBackend(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_class=ProductFilter
    search_fields=['name','category']
    ordering_fields=['price','name']
    ordering=['price']