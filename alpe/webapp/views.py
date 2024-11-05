from django.shortcuts import render
from .models import Client

def clients_list(request):
    # Retrieve all clients from MongoDB
    clients = Client.objects()
    return render(request, 'clients.html', {'clients': clients})
