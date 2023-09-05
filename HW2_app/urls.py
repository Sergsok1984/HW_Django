from django.urls import path
from .views import get_orders_by_client_id
from .views import get_products_by_client_id

urlpatterns = [
    path('get_orders/<int:client_id>/', get_orders_by_client_id),
    path('get_products/<int:client_id>/<str:period>/', get_products_by_client_id),
]
