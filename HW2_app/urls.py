from django.urls import path
from .views import get_orders_by_client_id, get_product_by_id, get_products_by_client_id, edit_product

urlpatterns = [
    path('get_orders/<int:client_id>/', get_orders_by_client_id),
    path('get_products/<int:client_id>/<str:period>/', get_products_by_client_id),
    path('edit_product/', edit_product),
    path('get_product/<int:product_id>/', get_product_by_id),
]
