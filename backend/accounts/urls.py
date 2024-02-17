from django.urls import path
from .views import *
from django.http import JsonResponse

def hello(request):
    return JsonResponse({'message': 'Hello!'})

urlpatterns = [
    path('', hello, name="home"),
<<<<<<< HEAD
    path('customer/register/', register_attempt, name="register_attempt"),
    path('customer/login/', login_attempt, name="login_attempt"),
    path('customer/token/', token_send, name="token_send"),
    path('customer/success/', success, name='success'),
    path('customer/verify/<str:auth_token>/', verify, name='verify'),
    path('customer/error/', error_page, name="error"),
    path('customer/logout/', logout_view, name='logout'),
    path('customer/reset_password/', password_reset, name='password_reset'),
    path('customer/reset_password/<str:auth_token>/', password_reset_confirm, name='password_reset_confirm'),
=======
    path('register/', register_attempt, name="register_attempt"),
    path('login/', login_attempt, name="login_attempt"),
    path('token/', token_send, name="token_send"),
    path('success/', success, name='success'),
    path('verify/<auth_token>/', verify, name="verify"),
    path('error/', error_page, name="error"),
    path('logout/', logout_view, name='logout'),
    path('reset_password/', password_reset, name='password_reset'),
    path('reset_password/<str:auth_token>/', password_reset_confirm, name='password_reset_confirm'),
>>>>>>> 63ebe147713dc8efa056fa0c8d239c035f1d5a0f
]
