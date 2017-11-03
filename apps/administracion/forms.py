from django.contrib.auth.models import User, Group
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.bootstrap import TabHolder, Tab


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    helper = FormHelper()
    helper.form_tag = False

    helper.layout = Layout(
        TabHolder(
            Tab(
                'Información Básica',
                'first_name',
                'last_name',
                'username',
                'password',
            ),
            Tab(
                'Grupo y Permisos',
                'groups',
                'is_staff',
                'is_superuser',
                'is_active',
                'date_joined'
            )
        )
    )

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['date_joined'].widget.attrs['readonly'] = True

    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'username': 'Usuario',
            'first_name': 'Nombre(s)',
            'last_name': 'Apellido(s)',
        }


class GroupForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Group
        fields = '__all__'
        labels = {
            'name': 'Nombre del Grupo'
        }
