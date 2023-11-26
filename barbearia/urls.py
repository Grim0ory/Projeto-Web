from django.urls import path
from . import views

urlpatterns = [
    path('principal', views.principal, name='principal'),
    path('opcoes', views.opcoes, name='opcoes'),
]