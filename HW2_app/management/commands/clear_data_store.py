from django.core.management import BaseCommand
from HW2_app.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Delete data in store'

    def handle(self, *args, **kwargs):
        Client.objects.all().delete()
        Product.objects.all().delete()
        Order.objects.all().delete()
