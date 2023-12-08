from myapp2.models import Product
import datetime
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = Product(name='Pasta', description='Italian pasta', price=450.00, quantity=1,
                       registration=datetime.date(2023, 12, 5))
        user.save()
        self.stdout.write(f'{user}')
