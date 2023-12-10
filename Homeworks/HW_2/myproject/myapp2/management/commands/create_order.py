from myapp2.models import Order, User, Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='User ID')
        parser.add_argument('product_id', type=int, nargs='+', help='Product ID')

    def handle(self, *args, **kwargs):
        user_id = kwargs['user_id']
        product_id = kwargs['product_id']

        user = User.objects.filter(pk=user_id).first()
        products = Product.objects.filter(pk__in=product_id)
        total_price = sum(product.price for product in products)

        if user and products:
            order = Order.objects.create(
                customer=user,
                total_price=total_price
            )
            order.products.set(products)
            order.save()
            self.stdout.write(f'Order created: {order}')
        else:
            self.stdout.write(f'User or Product not found. Order creation failed. '
                              f'\nUser: {user}'
                              f'\nProduct: {products}'
                              f'\nTotal price: {total_price}')
