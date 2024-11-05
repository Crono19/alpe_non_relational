# webapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.clients_list, name='clients_list'),
]
