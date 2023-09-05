from django.shortcuts import render
from .models import Client, Order
from datetime import datetime, timedelta


def get_orders_by_client_id(request, client_id):
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(client=client)
    orders_with_products = {}
    for order in orders:
        products = Order.objects.get(id=order.id).products.all()
        orders_with_products[order] = products

    context = {
        'client': client,
        'orders': orders_with_products,
    }
    return render(request, "HW2_app/client_orders.html", context)


def get_products_by_client_id(request, client_id: int, period: str):
    client = Client.objects.filter(pk=client_id).first()
    current_time = datetime.now()
    if period.lower() == 'hour':
        time_filter = current_time - timedelta(hours=1)
    elif period.lower() == 'week':
        time_filter = current_time - timedelta(weeks=1)
    elif period.lower() == 'month':
        time_filter = current_time - timedelta(days=30)
    elif period.lower() == 'year':
        time_filter = current_time - timedelta(days=365)
    else:
        time_filter = current_time - timedelta(days=365 * 100)

    orders = Order.objects.filter(client=client, date_create__gte=time_filter)

    products = []

    for order in orders:
        products.extend(Order.objects.get(id=order.id).products.all())

    context = {
        'client': client,
        'products': set(products),
    }
    return render(request, "HW2_app/client_products.html", context)
