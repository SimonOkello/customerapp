from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'manager/index.html', {})

def customer(request):
    return render(request, 'manager/customer.html', {})

def product(request):
    return render(request, 'manager/products.html', {})
