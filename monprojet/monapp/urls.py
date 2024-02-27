from django.urls import path
from monapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('furniture/', views.furniture, name='furniture'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.auth, name='login'),
    path('ajoute/', views.ajoute, name='ajoute'),
]
