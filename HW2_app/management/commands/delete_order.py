from django.core.management import BaseCommand
from HW2_app.models import Client, Order


class Command(BaseCommand):
    help = 'Delete order'

    def add_arguments(self, parser):
        parser.add_argument('client', type=str, help='client name')
        parser.add_argument('pk', type=int, help='order id')

    def handle(self, *args, **kwargs):
        client_name = kwargs.get('client')
        order_pk = kwargs.get('pk')
        client = Client.objects.filter(name=client_name).first()
        order = Order.objects.filter(pk=order_pk).first()
        if client is not None:
            orders = Order.objects.filter(client=client)
            for order_pk in orders:
                if order_pk == order:
                    order_pk.delete()
        self.stdout.write(f'order deleted')
