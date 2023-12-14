from django.urls import path
from .views import index, all_users, all_orders, order_full, order_week, order_month

urlpatterns = [
    path('', index, name='index'),
    path('all_users/', all_users, name='all_users'),
    path('client/<int:client_id>/', all_orders, name='all_orders'),
    path('order/<int:order_id>/', order_full, name='order_full'),
    path('client/<int:client_id>/order_week/', order_week, name='order_week'),
    path('client/<int:client_id>/order_month/', order_month, name='order_month'),
]
