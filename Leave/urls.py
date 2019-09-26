from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('',  views.home, name='home'),
    path('accounts/register/', views.usercreation, name='register'),
    path('accounts/login/', views.userpage, name='userpage'),
    path('accounts/login/userpage/', views.userauthentication, name='userauthentication'),
    ]