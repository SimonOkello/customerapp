from django.shortcuts import render
from .models import Product, Tag, Customer, Order

# Create your views here.


def index(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    customers_total = customers.count()
    orders_total = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'customers': customers, 'orders': orders, 'customers_total': customers_total,
               'orders_total': orders_total, 'delivered': delivered, 'pending': pending}
    return render(request, 'manager/index.html', context)


def customer(request):
    return render(request, 'manager/customer.html', {})


def product(request):
    products = Product.objects.all()
    return render(request, 'manager/products.html', {'products': products})
