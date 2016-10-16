from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper
import re
from django.core.exceptions import ObjectDoesNotExist

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Usuario',
            'first_name': 'Nombre(s)',
            'last_name': 'Apellido(s)',
            'email': 'Correo Electronico',
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = user.username
        user.save()
        return user

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

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2


class UserTest(forms.ModelForm):

    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = User
        fields = '__all__'


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = [
            'name',
        ]
        labels = {
            'name': 'Descripción',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }