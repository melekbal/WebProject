from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('girisPage/', views.girisPage, name='girisPage'),
    path('kayitPage/', views.kayitPage, name='kayitPage'),
    path('vetPage/', views.vetPage, name='vetPage'),
    path('iletisimPage/', views.iletisimPage, name='iletisimPage'),
]
