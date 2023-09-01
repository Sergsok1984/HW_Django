from django.core.management import BaseCommand
from HW2_app.models import Client, Order


class Command(BaseCommand):
    help = 'get orders by client name'

    def add_arguments(self, parser):
        parser.add_argument('client', type=str, help='client name')

    def handle(self, *args, **kwargs):
        client_name = kwargs.get('client')
        client = Client.objects.filter(name=client_name).first()
        if client:
            orders = Order.objects.filter(client=client)
            intro = f'All orders of client {client.name}\n'
            text = '\n'.join(f'{order.id=}  {order.sum_order=}  {order.products.name}' for order in orders)
            self.stdout.write(f'{intro}{text}')
