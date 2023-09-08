from django.contrib import admin

from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    ordering = ['name']
    list_filter = ['name']
    search_help_text = 'Поиск клиента по имени'

    fields = ['name', 'email', 'phone', 'date_reg']
    readonly_fields = ['name', 'date_reg']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    ordering = ['name']
    list_filter = ['name']
    search_help_text = 'Поиск продукта по названию'

    fields = ['name', 'description', 'price', 'quantity', 'image']
    readonly_fields = ['name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'sum_order', 'date_create']
    ordering = ['-date_create']
    list_filter = ['client']
    search_help_text = 'Поиск заказа по клиенту'

    fields = ['client', 'products', 'sum_order', 'date_create']
    readonly_fields = ['date_create']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
