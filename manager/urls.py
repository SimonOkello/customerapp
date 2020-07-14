from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import index, customer, product, createOrder, updateOrder, deleteOrder, registerPage, loginPage, logoutUser, userPage, accountSettings

# app_name = 'manager'

urlpatterns = [
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('user/', userPage, name='user_page'),
    path('user/account/', accountSettings, name='account'),
    path('', index, name='index'),
    path('customer/<str:pk>/', customer, name='customer'),
    path('products/', product, name='products'),
    path('create-order/<str:pk>/', createOrder, name='create_order'),
    path('update-order/<str:pk>/', updateOrder, name='update_order'),
    path('delete-order/<str:pk>/', deleteOrder, name='delete_order'),
    # PASSWORD RESET URLS
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='manager/password_reset.html'),
         name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='manager/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='manager/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='manager/password_reset_done.html'),
         name='password_reset_complete'),

]
