# webapp/views.py
from django.shortcuts import render
from .models import Client

def clients_list(request):
    clients = Client.objects()
    return render(request, 'clients.html', {'clients': clients})
