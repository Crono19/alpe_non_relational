# webapp/views.py
from django.shortcuts import render
from .models import Client
from .forms import CreateClient, UpdateClient

def clients_list(request):
    clients = Client.objects()
    return render(request, 'clients.html', {'clients': clients})

def create_client(request):
    form = CreateClient()

    context = {"form": form}
    return render(request, "create-client.html", context=context)

def update_client(request):
    form = UpdateClient()
    
    context = {"form": form}
    return render(request, "update-client.html", context=context)