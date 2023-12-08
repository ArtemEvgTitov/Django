from myapp2.models import Product
import datetime
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='Pasta', description='Italian pasta', price=450.00, quantity=1,
                       registration=datetime.date(2023, 12, 5))
        product.save()
        self.stdout.write(f'{product}')
