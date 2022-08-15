from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password


class Farmer(models.Model):
    """
    Farmer
    """
    username = models.CharField(verbose_name='username', max_length=150)
    password = models.CharField(verbose_name='password', max_length=128)
    email = models.EmailField(verbose_name='email address', unique=True)
    email_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    usertype = models.CharField(default='farmer', max_length=128)
    mobile = models.CharField(max_length=11, verbose_name='mobile', default='')
    first_name = models.CharField(verbose_name='first name', max_length=150, null=True, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=150, null=True, blank=True)

    class Meta:
        db_table = 'Farmer'
        verbose_name = 'Farmer'
        verbose_name_plural = verbose_name

    def set_password(self, password):
        self.password = make_password(password)
        return None

    def check_pwd(self, password):
        return check_password(password, self.password)


# class FarmerToken(models.Model):
#     """
#     FarmerToken
#     """
#     email = models.OneToOneField(Farmer, on_delete=models.CASCADE)
#     token = models.CharField(verbose_name='token', max_length=64)


class Customer(models.Model):
    """Customer"""
    username = models.CharField(verbose_name='username', max_length=150)
    password = models.CharField(verbose_name='password', max_length=128)
    email = models.EmailField(verbose_name='email address', unique=True)
    email_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    usertype = models.CharField(default='customer', max_length=128)
    mobile = models.CharField(max_length=11, unique=True, verbose_name='mobile', null=True, blank=True)
    first_name = models.CharField(verbose_name='first name', max_length=150, null=True, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=150, null=True, blank=True)

    class Meta:
        db_table = 'Customer'
        verbose_name = 'Customer'
        verbose_name_plural = verbose_name

    def set_password(self, password):
        self.password = make_password(password)
        return None

    def check_pwd(self, password):
        return check_password(password, self.password)


# class CustomerToken(models.Model):
#     """
#     FarmerToken
#     """
#     email = models.OneToOneField(Customer, on_delete=models.CASCADE)
#     token = models.CharField(verbose_name='token', max_length=64)


class Admin(models.Model):
    """
    Admin
    """
    username = models.CharField(verbose_name='username', max_length=150)
    password = models.CharField(verbose_name='password', max_length=128)
    email = models.EmailField(verbose_name='email address', unique=True)
    email_active = models.BooleanField(default=False)
    usertype = models.CharField(default='admin', max_length=128)

    def set_password(self, password):
        self.password = make_password(password)
        return None

    def check_pwd(self, password):
        return check_password(password, self.password)


# class AdminToken(models.Model):
#     """
#     Admin token
#     """
#     email = models.OneToOneField(Admin, on_delete=models.CASCADE)
#     token = models.CharField(verbose_name='token', max_length=64)


class Address(models.Model):
    """
    Customer address
    """
    customer_id = models.IntegerField(unique=True)
    address = models.CharField(max_length=50)
    receiver = models.CharField(max_length=20)
    postcode = models.CharField(max_length=6)
    city = models.CharField(max_length=20)

    class Meta:
        db_table = 'Customer address'
        verbose_name = 'Customer address'
        verbose_name_plural = verbose_name


