from django.db import models

from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    label=models.CharField(max_length=50)
    extra=models.JSONField(default=dict,blank=True)



class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True,default='')
    price=models.DecimalField(max_digits=8,decimal_places=2)
    in_stock=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)

    category=models.ForeignKey(Category,related_name='products',on_delete=models.PROTECT)
    tags=models.ManyToManyField(Tag,related_name='products',blank=True)