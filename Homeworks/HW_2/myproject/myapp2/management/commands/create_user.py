from myapp2.models import User
import datetime
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='Ivan', email='ivan@gmail.com', phone_number=89991234567, address='Murmansk, Lenina, 32',
                    registration=datetime.date(2023, 12, 8))
        user.save()
        self.stdout.write(f'{user}')
