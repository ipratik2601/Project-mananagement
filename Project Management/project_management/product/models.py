from itertools import product
from unicodedata import category
from venv import create
from django.db import models


# Create your models here.
# it gives table name as product_product 
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_description = models.TextField()
    product_qty = models.IntegerField()
    product_color = models.CharField(max_length=50,null=True)
    product_status = models.BooleanField(default=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)


#if want to give table name as your choice use "Meta" class 
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=50)
    category_description = models.TextField()
    class Meta:
        db_table = 'category'


