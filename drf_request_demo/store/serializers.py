from rest_framework import serializers
from .models import Category,Tag,Product
from django.db import transaction


# Basic serializer
class BasicSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    count=serializers.IntegerField(required=False,default=0)

class CategorySerializer(serializers.ModelSerializer):
    extra_info=serializers.CharField(read_only=True,default='N/A')
    class Meta:
        model=Category
        fields=['id','name','is_active','extra_info']

class UpperCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return super().to_representation(value).upper()

class TagSerializer(serializers.ModelSerializer):
    extra=serializers.DictField(child=serializers.CharField(),default=dict)
    class Meta:
        model=Tag
        fields=['id','label','extra']

class ProductSerializer(serializers.ModelSerializer):
    category=serializers.PrimaryKeyRelatedField(queryset=Category.objects.filter(is_active=True))
    tags=TagSerializer(many=True)

    discount=serializers.SerializerMethodField()
    name_upper=UpperCaseCharField(source='name')
    meta=serializers.JSONField(write_only=True,required=False)

    class Meta:
        model=Product
        fields=[
            'id','name','name_upper','description','price','in_stock',
            'created','category','tags','discount','meta'
        ]

    def get_discount(self,obj):
        return float(obj.price)*0.1
    
    def validate_price(self,value):
        if value<=0:
            raise serializers.ValidationError("price must be greater than 0.")
        return value
    
    def validate(self,data):
        if data.get('in_stock') and data.get('price')>10000:
            raise serializers.ValidationError("expensive items must be marked out of stock")
        return data
    
    def create(self, validated_data):
        meta=validated_data.pop('meta',{})
        tags_data=validated_data.pop('tags',{})
        with transaction.atomic():
            prod=Product.objects.create(**validated_data)
            for tag in tags_data:
                t,_=Tag.objects.get_or_create(**tag)
                prod.tags.add(t)
        return prod

    def update(self,instance, validated_data):
        tags_data=validated_data.pop('tags',None)
        for attr,val in validated_data.items():
            setattr(instance,attr,val)
        instance.save()

        if tags_data is not None:
            new_tags=[]
            for tag in tags_data:
                t,_=Tag.objects.get_or_create(**tag)
                new_tags.append(t)
            instance.tags.set(new_tags)
        return instance
    

class ProductHyperSerializer(serializers.HyperlinkedModelSerializer):
    category=serializers.HyperlinkedRelatedField(
        view_name='category-detail',queryset=Category.objects.all()
    )
    tags=serializers.HyperlinkedRelatedField(
        many=True,view_name='tag-detail',queryset=Tag.objects.all()
    )

    class Meta:
        model=Product
        fields=['url','id','name','category','tags']