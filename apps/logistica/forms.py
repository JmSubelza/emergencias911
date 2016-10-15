from django import forms
from apps.logistica.models import Incidente

class IncidenteForm(forms.ModelForm):

    class Meta:
        model = Incidente
        fields = [
            'time',
            'direccion',
            'descripcion',
            'estado',
            'lat',
            'log',
            'is_active',
        ]
        labels = {
            'time': 'Fecha y Hora',
            'direccion': 'Dirreccion',
            'descripcion': 'Descripcion',
            'estado': 'Estado',
            'lat': 'Latitud',
            'log': 'Longitud',
            'is_active': 'Activo',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }
