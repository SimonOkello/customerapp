from django.urls import path
from .views import index, customer, product, createOrder, updateOrder, deleteOrder, registerPage, loginPage, logoutUser, userPage


app_name = 'manager'

urlpatterns = [
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
     path('user/', userPage, name='user_page'),
    path('', index, name='index'),
    path('customer/<str:pk>/', customer, name='customer'),
    path('products/', product, name='products'),
    path('create-order/<str:pk>/', createOrder, name='create_order'),
    path('update-order/<str:pk>/', updateOrder, name='update_order'),
    path('delete-order/<str:pk>/', deleteOrder, name='delete_order'),

]
