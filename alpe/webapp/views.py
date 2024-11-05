# webapp/views.py
from django.shortcuts import render, get_object_or_404
from .models import Client, PhoneNumber
from .forms import CreateClient, UpdateClient
from bson import ObjectId
from django.shortcuts import render

def clients_list(request):
    clients = Client.objects()
    return render(request, 'clients.html', {'clients': clients})

def view_client(request, pk):

    client = Client.objects(id=pk).first()
    if client is None:
        return render(request, "404.html", status=404)

    context = {"client": client}
    return render(request, "view-client.html", context=context)

def view_client_phonenumbers(request, pk):
    client = get_object_or_404(Client, id=pk)
    phone_numbers = client.phone_numbers.filter(deleted=False)
    return render(request, "view-client-phone.html", {
        'client': client,
        'phone_numbers': phone_numbers
    })

def create_client(request):
    form = CreateClient()

    context = {"form": form}
    return render(request, "create-client.html", context=context)

def update_client(request, pk):
    form = UpdateClient()

    context = {"form": form}
    return render(request, "update-client.html", context=context)