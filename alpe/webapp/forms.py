# webapp/forms.py
from django import forms
from .models import PhoneNumber

class CreateClient(forms.Form):
    code = forms.CharField(label="Código", max_length=100)
    nit = forms.CharField(label="NIT", max_length=100)
    name = forms.CharField(label="Nombre", max_length=100)
    direction = forms.CharField(label="Dirección", max_length=255, required=False)

class UpdateClient(forms.Form):
    code = forms.CharField(label="Código", max_length=100)
    nit = forms.CharField(label="NIT", max_length=100)
    name = forms.CharField(label="Nombre", max_length=100)
    direction = forms.CharField(label="Dirección", max_length=255, required=False)

class AddClientPhones(forms.Form):
    number = forms.CharField(label="Teléfono", max_length=15)
