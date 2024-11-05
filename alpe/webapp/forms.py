# webapp/forms.py
from django import forms

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

class AddClientPhones(forms.ModelForm):
    class Meta:
        fields = ["phone"]
        labels = {"phone": "Teléfono"}
