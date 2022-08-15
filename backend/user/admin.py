from django.contrib import admin
from .models import Farmer, Customer, Address


# Register your models here.
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'mobile', 'email_active')

    '''filter options'''
    list_filter = ('email_active',)

    '''10 items per page'''
    list_per_page = 10


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'mobile', 'email_active')

    '''filter options'''
    list_filter = ('email_active',)

    '''10 items per page'''
    list_per_page = 10


class AddressAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'address', 'receiver', 'postcode', 'city')

    '''filter options'''
    # list_filter = ('email_active',)

    '''10 items per page'''
    list_per_page = 10


admin.site.register(Farmer, FarmerAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address, AddressAdmin)


