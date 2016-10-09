from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms


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
            'username' : 'Usuario',
            'first_name' : 'Nombre(s)',
            'last_name' : 'Apellido(s)',
            'email': 'Correo Electronico',
        }


class GroupCreate(forms.ModelForm):

    class Meta:
        model = Group
        fields = [
            'name',
        ]
        labels = {
            'name' : 'Descripcion',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }