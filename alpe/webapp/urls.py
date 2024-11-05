# webapp/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_list, name='clients_list'),
    path("create-client", views.create_client, name="create-client"),
    path("update-client/<str:pk>", views.update_client, name="update-client"),
    path("client/<str:pk>", views.view_client, name="client"),  #
]
