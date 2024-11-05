from .models import Client
from django import forms

# Create client
class CreateClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["code", "nit", "name", "direction"]
        labels = {
            "code": "Código",
            "nit": "NIT",
            "name": "Nombre",
            "direction": "Dirección",
        }


# Update client
class UpdateClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["code", "nit", "name", "direction"]
        labels = {
            "code": "Código",
            "nit": "NIT",
            "name": "Nombre",
            "direction": "Dirección",
        }