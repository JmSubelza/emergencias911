from django import forms
from crispy_forms.helper import FormHelper
from apps.servicios.models import Vehiculo, TipoVehiculo, CentroEmergencia, DispositivoGPS


class VehiculoForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

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


class TipoVehiculoForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

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


class CentroEmergenciaForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = CentroEmergencia
        fields = [
            'name',
            'direccion',
            'telefono',
            'lat',
            'lng',
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
            'lng': 'Longitud',
            'sector': 'Sector',
            'nivel': 'Nivel',
            'tipo': 'Tipo',
            'is_active': 'Activo',
        }


class DispositivoGpsForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = DispositivoGPS
        fields = [
            'name',
            'imei',
            'nro_sim',
            'lat',
            'lng',
            'time',
            'is_active',
        ]
        labels = {
            'name': 'Descripción',
            'imei': 'IMEI Dispositivo',
            'nro_sim': 'Numero de Teléfono',
            'lat': 'Latitud',
            'lng': 'Longitud',
            'time': 'Fecha y Hora',
            'is_active': 'Activo',
        }
