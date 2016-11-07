from django import forms
from apps.logistica.models import Incidente, TipoIncidente, AsignacionIncidente
from crispy_forms.helper import FormHelper, Layout


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
            'is_active',
        ]
        labels = {
            'direccion': 'Dirreccion',
            'descripcion': 'Descripcion',
            'estado': 'Estado',
            'lat': 'Latitud',
            'lng': 'Longitud',
            'tipo': 'Tipo',
            'is_active': 'Activo',
        }


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
