from django.contrib.auth.models import User, Group, GroupManager
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.administracion.forms import UserForm, GroupForm


# Create your views here.


class UsuarioList(ListView):
    model = User
    template_name = 'administracion/usuario_list.html'

    def get_queryset(self):
        # Filtra por activo o inactivo
        super(UsuarioList, self).get_queryset()
        c = User.objects.all()

        if self.request.GET.get('is_active') == '1':
            c = c.filter(is_active=True)
        elif self.request.GET.get('is_active') == '0':
            c = c.filter(is_active=False)
        return c

class UsuarioCreate(CreateView):
    model = User
    template_name = 'administracion/usuario_form.html'
    form_class = UserForm
    success_url = reverse_lazy('administracion:usuario')


class UsuarioUpdate(UpdateView):
    model = User
    template_name = 'administracion/usuario_form.html'
    form_class = UserForm
    success_url = reverse_lazy('administracion:usuario')


class UsuarioDelete(DeleteView):
    model = User
    template_name = 'administracion/usuario_delete.html'
    success_url = reverse_lazy('administracion:usuario')


class GrupoList(ListView):
    model = Group
    template_name = 'administracion/grupo_list.html'


class GrupoCreate(CreateView):
    model = Group
    template_name = 'administracion/grupo_form.html'
    form_class = GroupForm
    success_url = reverse_lazy('administracion:grupo')


class GrupoUpdate(UpdateView):
    model = Group
    template_name = 'administracion/grupo_form.html'
    form_class = GroupForm
    success_url = reverse_lazy('administracion:grupo')


class GrupoDelete(DeleteView):
    model = Group
    template_name = 'administracion/grupo_delete.html'
    success_url = reverse_lazy('administracion:grupo')
