from django.contrib import admin
from ordersManagement.models import Client, Item, Order

# Register your models here.

class ClientsAdminPanel(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = (['name'])

class ItemsAdminPanel(admin.ModelAdmin):
    list_display = ('name', 'section', 'price')
    list_filter = (['section'])

class OrdersAdminPanel(admin.ModelAdmin):
    list_display = ('number', 'deliveryDate', 'delivered')
    list_filter = (['deliveryDate'])
    date_hierarchy = 'deliveryDate'

admin.site.register(Client, ClientsAdminPanel)
admin.site.register(Item, ItemsAdminPanel)
admin.site.register(Order, OrdersAdminPanel)