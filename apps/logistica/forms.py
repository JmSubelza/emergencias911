from django import forms
from apps.logistica.models import Incidente
from datetime import datetime


class IncidenteForm(forms.ModelForm):

    lat = forms.DecimalField(min_value=0, max_value=8, decimal_places=6, initial="-17.783308",
                             required=False, widget=forms.TextInput(attrs={'class': 'form-control required'}))
    log = forms.DecimalField(min_value=0, max_value=8, decimal_places=6, initial="-63.182118",
                             required=False, widget=forms.TextInput(attrs={'class': 'form-control required'}))

    class Meta:
        model = Incidente
        fields = [
            'direccion',
            'descripcion',
            'estado',
            'lat',
            'log',
            'is_active',
        ]
        labels = {
            'direccion': 'Dirreccion',
            'descripcion': 'Descripcion',
            'estado': 'Estado',
            'lat': 'Latitud',
            'log': 'Longitud',
            'is_active': 'Activo',
        }
        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }
