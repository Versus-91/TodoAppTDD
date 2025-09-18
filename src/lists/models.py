
from django.db import models

# Create your models here.
class List(models.Model):
    pass
class Item(models.Model):
    description = models.TextField(default='')
    list = models.ForeignKey(List,default=None, on_delete=models.CASCADE)
class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(max_length=255)