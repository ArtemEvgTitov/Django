from myapp2.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com', password='secret', age=25)
        user = User(name='Neo', email='neo@example.com', password='secret', age=58)
        user.save()
        self.stdout.write(f'{user}')
