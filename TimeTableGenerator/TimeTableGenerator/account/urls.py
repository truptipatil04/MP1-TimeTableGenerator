from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('info/',views.info,name='info'),
    path('logout/',views.logout,name='logout'),
    path('contact/',views.contact,name='contact'),
    path('generate/',views.generate,name='generate')
]