from django import forms
from apps.logistica.models import Incidente, TipoIncidente, AsignacionIncidente
from crispy_forms.helper import FormHelper, Layout


class IncidenteForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_tag = False

    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':15}))
    lat = forms.DecimalField(max_value=8, decimal_places=6, initial="-17.783308", required=False,)
    log = forms.DecimalField(max_value=8, decimal_places=6, initial="-63.182118", required=False,)

    class Meta:
        model = Incidente
        fields = [
            'direccion',
            'descripcion',
            'tipo',
            'lat',
            'log',
            'estado',
            'is_active',
        ]
        labels = {
            'direccion': 'Dirreccion',
            'descripcion': 'Descripcion',
            'estado': 'Estado',
            'lat': 'Latitud',
            'log': 'Longitud',
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
