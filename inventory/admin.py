from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = 'Inventory Dashboard'

class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'category', 'quantity')
  list_filter = ('category',)

class OrderAdmin(admin.ModelAdmin):
  list_display = ('product', 'staff', 'date')
  list_filter = ('product', 'staff', 'date')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.unregister(Group)