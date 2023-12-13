from myapp3.models import User
import datetime
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create user."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('email', type=str, help='User email')
        parser.add_argument('phone_number', type=int, help='User phone number')
        parser.add_argument('address', type=str, help='User address')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        email = kwargs['email']
        phone_number = kwargs['phone_number']
        address = kwargs['address']

        user = User(name=name, email=email, phone_number=phone_number, address=address,
                    registration=datetime.date.today())
        user.save()
        self.stdout.write(f'Create: {user}')
