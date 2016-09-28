from django import forms
from apps.servicios.models import Vehiculo, TipoVehiculo


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
            'placa',
            'name',
            'marca',
            'modelo',
            'nro_motor',
            'nro_chasis',
            'sector',
            'tipo_id',
            'is_active',
        ]
        labels = {
            'placa': 'Placa',
            'name': 'Nombre',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'nro_motor': 'Número Motor',
            'nro_chasis': 'Número Chasis',
            'sector': 'Sector',
            'tipo_id': 'Tipo Vehiculo',
            'is_active': 'Activo',
        }
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'nro_motor': forms.TextInput(attrs={'class': 'form-control'}),
            'nro_chasis': forms.TextInput(attrs={'class': 'form-control'}),
            'sector': forms.Select(attrs={'class': 'form-control'}),
            'tipo_id': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }


class TipoVehiculoForm(forms.ModelForm):
    class Meta:
        model = TipoVehiculo
        fields = [
            'name',
            'is_active',
        ]
        labels = {
            'name': 'Descripción',
            'is_active': 'Activo',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }

