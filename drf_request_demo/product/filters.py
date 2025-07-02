import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    max_price=django_filters.NumberFilter(field_name='price',lookup_expr='lte')


    class Meta:
        model=Product
        fields=['category','in_stock','max_price']