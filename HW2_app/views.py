from django.shortcuts import render
from .models import Client, Order, Product
from datetime import datetime, timedelta
from .forms import EditProductForm
from django.core.files.storage import FileSystemStorage


def get_product_by_id(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    context = {
        'title': 'Продукт',
        'message': 'Описание продукта',
        'product': product,
    }
    return render(request, "store_app/product.html", context)


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


def edit_product(request):
    message = 'Продукт не был изменён'
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES)
        if form.is_valid():
            edited_product = form.cleaned_data['edited_product']
            if form.cleaned_data['name']:
                edited_product.name = form.cleaned_data['name']
                message = 'Продукт изменён'
            if form.cleaned_data['description']:
                edited_product.description = form.cleaned_data['description'],
                message = 'Продукт изменён'
            if form.cleaned_data['price']:
                edited_product.price = form.cleaned_data['price']
                message = 'Продукт изменён'
            if form.cleaned_data['quantity']:
                edited_product.quantity = form.cleaned_data['quantity']
                message = 'Продукт изменён'
            if form.cleaned_data['date_add']:
                edited_product.date_add = form.cleaned_data['date_add']
                message = 'Продукт изменён'
            if form.cleaned_data['image']:
                image = form.cleaned_data['image']
                fs = FileSystemStorage()
                fs.save(image.name, image)
                edited_product.image = image
                message = 'Продукт изменён'

            if message == 'Продукт изменён':
                edited_product.save()
    else:
        message = 'Выберите продукт и задайте новые значения его свойств.'
        form = EditProductForm()
    return render(request, 'store_app/edit_product.html',
                  {'form': form, 'message': message, 'title': 'Изменение продукта, добавление фотографии'})
