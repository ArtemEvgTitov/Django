from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField()

    def __str__(self):
        return f'Product name: {self.name}\nPrice: {self.price}\nDescription: {self.description}'
