from myapp2.models import Order, User, Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='User ID')
        parser.add_argument('product_id', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        user_id = kwargs['user_id']
        product_id = kwargs['product_id']

        user = User.objects.filter(pk=user_id).first()
        product = Product.objects.filter(pk=product_id).first()

        if user and product:
            order = Order(customer=user, product=product, total_price=450.00)
            order.save()
            self.stdout.write(f'Order created: {order}')
        else:
            self.stdout.write('User or Product not found. Order creation failed.')
