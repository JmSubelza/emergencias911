# encoding:utf-8
from django import forms
from crispy_forms.helper import FormHelper
from .models import Device
from django.utils import timezone


class DispositivoGpsForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Device
        fields = [
            'name',
            'phone_number',
            'imei',
            'lat',
            'lng',
            'time',
            'is_active',
        ]
        labels = {
            'name': 'Descripción',
            'phone_number': 'Numero de telefono',
            'imei': 'IMEI Dispositivo',
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
