from django.core.management import BaseCommand
from HW2_app.models import Client


class Command(BaseCommand):
    help = 'Create client'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Client_name')
        parser.add_argument('email', type=str, help='Email')
        parser.add_argument('phone', type=str, help='Phone')
        parser.add_argument('address', type=str, help='Address')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')
        client = Client(
            name=name,
            email=email,
            phone=phone,
            address=address,
        )
        client.save()
        self.stdout.write('client created')
