from django.urls import path
from .views import index, customer, product

urlpatterns = [
    path('', index, name='index'),
    path('customer/', customer, name = 'customer'),
    path('products/', product, name='product'),

]