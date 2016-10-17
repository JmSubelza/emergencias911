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

    lat = forms.DecimalField(max_value=8, decimal_places=6, initial="-17.783308", required=False,)
    log = forms.DecimalField(max_value=8, decimal_places=6, initial="-63.182118", required=False,)

    helper = FormHelper()
    helper.form_tag = False

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
            'log',
            'time',
            'is_active',
        ]
        labels = {
            'name': 'Descripción',
            'imei': 'IMEI Dispositivo',
            'nro_sim': 'Numero de Teléfono',
            'lat': 'Latitud',
            'log': 'Longitud',
            'time': 'Fecha y Hora',
            'is_active': 'Activo',
        }
