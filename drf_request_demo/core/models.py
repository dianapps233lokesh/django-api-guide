from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=100)


class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)