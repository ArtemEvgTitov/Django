from django.shortcuts import render, get_object_or_404
from .models import User, Order
import datetime
from datetime import timedelta


def index(request):
    return render(request, 'myapp3/index.html')


def all_users(request):
    count = 1
    users = {}
    while True:
        try:
            user = get_object_or_404(User, pk=count)
            users[count] = user.name
            count += 1
        except:
            context = {'users': users}
            return render(request, 'myapp3/all_users.html', context)


def all_orders(request, client_id):
    client = get_object_or_404(User, pk=client_id)
    orders = Order.objects.filter(customer=client).order_by('date_ordered')
    return render(request, 'myapp3/all_orders.html', {'client': client, 'orders': orders})


def order_full(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'myapp3/order_full.html', {'order': order})



def order_week(request, client_id):
    client = get_object_or_404(User, pk=client_id)
    orders = Order.objects.filter(customer=client,
                                  date_ordered__gte=datetime.datetime.now() - timedelta(days=7)).order_by(
        'date_ordered')
    return render(request, 'myapp3/order_week.html', {'client': client, 'orders': orders})


def order_month(request, client_id):
    client = get_object_or_404(User, pk=client_id)
    orders = Order.objects.filter(customer=client,
                                  date_ordered__gte=datetime.datetime.now() - timedelta(days=30)).order_by(
        'date_ordered')
    return render(request, 'myapp3/order_month.html', {'client': client, 'orders': orders})
