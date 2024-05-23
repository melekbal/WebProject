from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('girisPage/', views.girisPage, name='girisPage'),
    path('kayitPage/', views.kayitPage, name='kayitPage'),
    path('vetPage/', views.vetPage, name='vetPage'),
    path('iletisimPage/', views.iletisimPage, name='iletisimPage'),
    path('kullaniciPage/', views.kullaniciPage, name='kullaniciPage'),
    path('ilacPage/', views.ilacPage, name='ilacPage'),
<<<<<<< HEAD
    path('notPage/', views.notPage, name='notPage'),
=======
>>>>>>> 45df169eca064828fa0865a4706e0498fb3a5a70


]
