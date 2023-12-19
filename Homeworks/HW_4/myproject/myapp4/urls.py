from django.urls import path
from .views import index, product_form

urlpatterns = [
    path('', index, name='index'),
    path('product_form/', product_form, name='product_form'),
]
