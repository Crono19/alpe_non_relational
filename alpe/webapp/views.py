# webapp/views.py
from django.shortcuts import render
from .models import Client
from .forms import CreateClient, UpdateClient
from bson import ObjectId
from django.shortcuts import render, get_object_or_404

def clients_list(request):
    clients = Client.objects()
    return render(request, 'clients.html', {'clients': clients})

def view_client(request, pk):
    try:
        client_id = ObjectId(pk)
    except Exception:
        return render(request, "404.html", status=404)

    client = Client.objects(id=client_id).first()
    if client is None:
        return render(request, "404.html", status=404)

    context = {"client": client}
    return render(request, "view-client.html", context=context)

def create_client(request):
    form = CreateClient()

    context = {"form": form}
    return render(request, "create-client.html", context=context)

def update_client(request, pk):
    form = UpdateClient()

    context = {"form": form}
    return render(request, "update-client.html", context=context)