from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    code=models.TextField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='snippets')