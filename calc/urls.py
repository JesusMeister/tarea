from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('usuarios',views.usuarios, name='usuarios'),
    path('partidas',views.partidas, name='partidas'),
]