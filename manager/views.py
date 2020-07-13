from django.shortcuts import render, get_object_or_404, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import Product, Tag, Customer, Order
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from .decorators import unauthenticated_user

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+username)
            return redirect('manager:login')
    context = {'form': form}
    return render(request, 'manager/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('manager:index')
        else:
            messages.error(request, 'Username/Password Incorrect')
            return redirect('manager:login')

    return render(request, 'manager/login.html', {})


def logoutUser(request):
    logout(request)
    return redirect('manager:login')


def userPage(request):
    context = {}
    return render(request, 'manager/user.html', context)


@login_required(login_url='manager:login')
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


@login_required(login_url='manager:login')
def customer(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {'customer': customer, 'orders': orders,
               'total_orders': total_orders, 'myFilter': myFilter}
    return render(request, 'manager/customer.html', context)


@login_required(login_url='manager:login')
def product(request):
    products = Product.objects.all()
    return render(request, 'manager/products.html', {'products': products})


@login_required(login_url='manager:login')
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=('product', 'status'))
    customer = get_object_or_404(Customer, id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('manager:index')
    context = {'formset': formset}
    return render(request, 'manager/order_form.html', context)


@login_required(login_url='manager:login')
def updateOrder(request, pk):
    order = get_object_or_404(Order, id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('manager:index')
    context = {'form': form}
    return render(request, 'manager/order_form.html', context)


@login_required(login_url='manager:login')
def deleteOrder(request, pk):
    order = get_object_or_404(Order, id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('manager:index')
    return render(request, 'manager/delete.html', {'order': order})
