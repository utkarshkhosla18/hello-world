from django.db import models
from user.models import *


class Category(models.Model):
    """
    Category
    """
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'Category'
        verbose_name = 'Category'
        verbose_name_plural = verbose_name


class Product(models.Model):
    """
    Product
    """
    category = models.ForeignKey(Category, related_name='category_products', on_delete=models.CASCADE)
    farmer = models.ForeignKey('user.Farmer', related_name='farmer_products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(blank=True, null=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    STATUS = ((0, 'out of stock'),
              (1, 'on stock'))
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        db_table = 'Product'
        verbose_name = 'Product'
        verbose_name_plural = verbose_name


class Cart(models.Model):
    """
    Cart
    """
    customer = models.ForeignKey('user.Customer', related_name='customer_carts', on_delete=models.CASCADE)
    product = models.IntegerField()
    quantity = models.IntegerField()


