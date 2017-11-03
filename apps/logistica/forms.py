from django import forms
from apps.logistica.models import Incidente, TipoIncidente, AsignacionIncidente
from crispy_forms.helper import FormHelper, Layout
from django.utils import timezone


class IncidenteForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 15}))

    class Meta:
        model = Incidente
        fields = [
            'descripcion',
            'tipo',
            'lat',
            'lng',
            'estado',
            'time',
            'is_active',

        ]
        labels = {
            'direccion': 'Dirreccion',
            'descripcion': 'Descripcion',
            'estado': 'Estado',
            'lat': 'Latitud',
            'lng': 'Longitud',
            'tipo': 'Tipo',
            'time': 'Fecha y Hora',
            'is_active': 'Activo',
        }

    def __init__(self, *args, **kwargs):
        super(IncidenteForm, self).__init__(*args, **kwargs)
        self.fields['lat'].widget.attrs['readonly'] = True
        self.fields['lng'].widget.attrs['readonly'] = True
        self.fields['time'].widget.attrs['readonly'] = True
        self.fields['lat'].initial = '-17.783308'
        self.fields['lng'].initial = '-63.182118'
        self.fields['time'].initial = timezone.now()


class TipoIncidenteForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = TipoIncidente
        fields = '__all__'
        labels = {
            'name': 'Descripción',
            'is_active': 'Activo',
        }


class AsignacionIncidenteForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = AsignacionIncidente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AsignacionIncidenteForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget.attrs['readonly'] = True
        self.fields['time'].initial = timezone.now()