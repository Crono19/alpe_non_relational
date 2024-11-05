# webapp/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_list, name='clients_list'),
    path("create-client", views.create_client, name="create-client"),
    path("client/<str:pk>", views.view_client, name="client"),
    path("update-client/<str:pk>", views.update_client, name="update-client"),
    path("delete-client/<str:pk>", views.delete_client, name="delete-client"),
    path("client-phonenumbers/<str:pk>", views.view_client_phonenumbers, name="client-phonenumbers"),
    path("add-client-phonenumber/<str:pk>", views.add_client_phonenumber, name="add-client-phonenumber"),
]
