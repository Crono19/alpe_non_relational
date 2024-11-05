# webapp/views.py
from django.shortcuts import render, redirect
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