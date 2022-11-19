from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('',views.register,name='register'),
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('info',views.info,name='info')
]