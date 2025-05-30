"""Définitions des URL pour l'application profiles."""
from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile_detail, name='profile'),
]
