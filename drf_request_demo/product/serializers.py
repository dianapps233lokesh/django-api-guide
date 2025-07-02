from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','category','price','in_stock','owner']
        read_only_fields = ['id', 'owner']