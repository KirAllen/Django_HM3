from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404
from .models import Customer, Order

def index(request):
    return render(request, "app2/index.html")


def basket(request, user_id):
    products = []
    customer = Customer.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(customer=customer).all()
    for order in orders:
        products.append(order.products.all())
    products.reverse()
    return render(request, 'myapp2/user_all_orders.html', {'customer': customer, 'orders': orders, 'products': products})


def sorted_basket(request, customer_id, days_ago):
    products = []
    product_set=[]
    now = datetime.now()
    before = now - timedelta(days=days_ago)
    customer = Customer.objects.filter(pk=customer_id).first()
    orders = Order.objects.filter(customer=customer, date_ordered__range=(before, now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)

    return render(request, 'app2/user_all_product.html', {'customer': customer, 'products': products, 'days': days_ago})