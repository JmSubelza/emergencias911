from django.contrib.auth.models import User, Group
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
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

    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'username': 'Usuario',
            'first_name': 'Nombre(s)',
            'last_name': 'Apellido(s)',
        }

    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username

    def clean_email(self):
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Correo Electronico ya registrado.')
        return email


class GroupForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Group
        fields = '__all__'
        labels = {
            'name': 'Nombre del Grupo'
        }
