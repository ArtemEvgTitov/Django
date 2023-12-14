import datetime
from datetime import timedelta
import random

from myapp3.models import Order, User, Product
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count')

    def handle(self, *args, **kwargs):

        count = kwargs.get('count')

        for i in range(1, count + 1):
            client_id = random.randint(1, 4)
            client = User.objects.filter(pk=client_id).first()
            quantity = random.randint(1, 3)
            products = []
            for i in range(1, quantity + 1):
                product_id = random.randint(1, 3)
                product = Product.objects.filter(pk=product_id).first()
                products.append(product)
            total_price = sum(product.price for product in products)
            days = random.randint(1, 364)
            order = Order.objects.create(
                customer=client,
                total_price=total_price,
                date_ordered=datetime.datetime.now() - timedelta(days=days)
            )
            order.products.set(products)
            order.save()
            self.stdout.write(f'Order created: {order}')
