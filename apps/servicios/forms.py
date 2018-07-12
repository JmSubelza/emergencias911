# encoding:utf-8
from django import forms
from crispy_forms.helper import FormHelper
from .models import Vehiculo, TipoVehiculo, CentroEmergencia, DispositivoGPS, TipoCentroEmergencia
from django.utils import timezone


class VehiculoForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Vehiculo
        fields = [
            'placa',
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
            'marca': 'Marca',
            'modelo': 'Modelo',
            'nro_motor': 'Número Motor',
            'nro_chasis': 'Número Chasis',
            'sector': 'Sector',
            'tipo_id': 'Tipo Vehiculo',
            'gps_id': 'Dispositivo GPS',
            'is_active': 'Activo',
        }

    def __init__(self, *args, **kwargs):
        super(VehiculoForm, self).__init__(*args, **kwargs)
        if not kwargs['instance'] is None:
            _queryset = DispositivoGPS.objects.exclude(
                id__in=[x.gps_id.id for x in Vehiculo.objects.all() if x.id != kwargs['instance'].id])
        else:
            _queryset = DispositivoGPS.objects.exclude(id__in=[x.gps_id.id for x in Vehiculo.objects.all()])
        self.fields["gps_id"].queryset = _queryset


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


class TipoCentroEmergenciaForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = TipoCentroEmergencia
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
            'tipo_id',
            'is_active',
        ]
        labels = {
            'name': 'Nombre',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'lat': 'Latitud',
            'lng': 'Longitud',
            'sector': 'Sector',
            'tipo_id': 'Tipo',
            'is_active': 'Activo',
        }

    def __init__(self, *args, **kwargs):
        super(CentroEmergenciaForm, self).__init__(*args, **kwargs)
        self.fields['lat'].widget.attrs['readonly'] = True
        self.fields['lng'].widget.attrs['readonly'] = True
        self.fields['lat'].initial = '-17.783308'
        self.fields['lng'].initial = '-63.182118'


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

    def __init__(self, *args, **kwargs):
        super(DispositivoGpsForm, self).__init__(*args, **kwargs)
        self.fields['lat'].widget.attrs['readonly'] = True
        self.fields['lng'].widget.attrs['readonly'] = True
        self.fields['time'].widget.attrs['readonly'] = True
        self.fields['lat'].initial = '-17.783308'
        self.fields['lng'].initial = '-63.182118'
        self.fields['time'].initial = timezone.now()
