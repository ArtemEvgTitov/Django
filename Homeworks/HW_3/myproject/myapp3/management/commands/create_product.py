from myapp3.models import Product
import datetime
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product1 = Product(name='Pasta', description='Italian pasta', price=450.00, quantity=1,
                           registration=datetime.date.today())
        product1.save()
        self.stdout.write(f'{product1}')

        product2 = Product(name='Pizza', description='Italian pizza', price=650.00, quantity=1,
                           registration=datetime.date.today())
        product2.save()
        self.stdout.write(f'{product2}')

        product3 = Product(name='Сroissant', description='French croissant', price=350.00, quantity=1,
                           registration=datetime.date.today())
        product3.save()
        self.stdout.write(f'{product3}')
