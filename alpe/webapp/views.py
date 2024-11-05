# webapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, PhoneNumber
from .forms import CreateClient, UpdateClient, AddClientPhones
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
    client = Client.objects(id=pk).first()
    phone_numbers = client.phone_numbers
    return render(request, "client-phonenumbers.html", {
        'client': client,
        'phone_numbers': phone_numbers
    })

def create_client(request):
    if request.method == 'POST':
        form = CreateClient(request.POST)
        if form.is_valid():
            # Extrae los datos del formulario
            code = form.cleaned_data['code']
            nit = form.cleaned_data['nit']
            name = form.cleaned_data['name']
            direction = form.cleaned_data.get('direction', '')

            # Crea la lista de números de teléfono
            phone_numbers = []
            phone_number_data = form.cleaned_data.get('phone_numbers')
            if phone_number_data:
                for number in phone_number_data:
                    phone_numbers.append(PhoneNumber(number=number))

            # Crea y guarda el cliente
            client = Client(
                code=code,
                nit=nit,
                name=name,
                direction=direction,
                phone_numbers=phone_numbers
            )
            client.save()  # Guarda el cliente en MongoDB
            
            # Redirige a la lista de clientes (asegúrate de tener una URL para esto)
            return redirect('clients_list')  # Cambia 'client_list' a la URL o vista de tu lista de clientes
    else:
        form = CreateClient()

    context = {"form": form}
    return render(request, "create-client.html", context=context)

def update_client(request, pk):
    form = UpdateClient()

    context = {"form": form}
    return render(request, "update-client.html", context=context)

def add_client_phonenumber(request, pk):
    client = Client.objects(id=pk).first()
    form = AddClientPhones()

    context = {"form": form, "client": client}
    return render(request, "alpe_corporation/add-client-phone.html", context=context)