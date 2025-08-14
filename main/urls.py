from django.contrib import admin
from django.urls import path

from main import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('delivery/', views.delivery, name='delivery'),
    path('contact/', views.contact, name='contact'),
]