from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    in_stock=models.BooleanField(default=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name