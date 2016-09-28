from django import forms
from apps.servicios.models import Vehiculo, TipoVehiculo, CentroEmergencia


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
            'gps_id',
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
            'gps_id': 'Dispositivo GPS',
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
            'gps_id': forms.Select(attrs={'class': 'form-control'}),
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


class CentroEmergenciaForm(forms.ModelForm):
    class Meta:
        model = CentroEmergencia
        fields = [
            'name',
            'direccion',
            'telefono',
            'lat',
            'log',
            'sector',
            'nivel',
            'tipo',
            'is_active',
        ]
        labels = {
            'name': 'Descripción',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'lat': 'Latitud',
            'log': 'Longitud',
            'sector': 'Sector',
            'nivel': 'Nivel',
            'tipo': 'Tipo',
            'is_active': 'Activo',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'lat': forms.TextInput(attrs={'class': 'form-control'}),
            'log': forms.TextInput(attrs={'class': 'form-control'}),
            'sector': forms.Select(attrs={'class': 'form-control'}),
            'nivel': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }

