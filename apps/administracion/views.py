from django.contrib.auth.models import User, Group
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.administracion.forms import UserForm, GroupCreate
# Create your views here.


class UsuarioList(ListView):
    model = User
    template_name = 'administracion/usuario_list.html'


class UsuarioCreate(CreateView):
    model = User
    template_name = 'administracion/usuario_form.html'
    form_class = UserForm
    success_url = reverse_lazy('administracion:usuario_crear')


class GrupoList(ListView):
    model = Group
    template_name = 'administracion/grupo_list.html'


class GrupoCreate(CreateView):
    model = Group
    template_name = 'administracion/grupo_form.html'
    form_class = GroupCreate
    success_url = reverse_lazy('administracion:usuario_crear')

