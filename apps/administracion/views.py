from django.contrib.auth.models import User, Group
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from apps.administracion.forms import UserForm, GroupForm
from django.contrib import messages


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


class UsuarioDetail(DetailView):
    model = User
    template_name = 'administracion/user_detail.html'


class UsuarioCreate(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'administracion/usuario_form.html'
    form_class = UserForm
    success_url = reverse_lazy('administracion:usuario')
    success_message = "El usuario '%(username)s' fue creado con éxito"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(form.cleaned_data['password'])
        obj.save()
        return super(UsuarioCreate, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            username=self.object.username,
        )


class UsuarioUpdate(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'administracion/usuario_form.html'
    form_class = UserForm
    success_url = reverse_lazy('administracion:usuario')
    success_message = "El usuario '%(username)s' fue modificado con éxito"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(form.cleaned_data['password'])
        obj.save()
        return super(UsuarioUpdate, self).form_valid(form)


class UsuarioDelete(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'administracion/usuario_delete.html'
    success_url = reverse_lazy('administracion:usuario')
    success_message = "El usuario '%(username)s' fue eliminado con éxito"

    def delete(self, request, *args, **kwargs):
        messages.success(
            request, 'El usuario fue eliminado')
        return super(UsuarioDelete, self).delete(
            request, *args, **kwargs)

class GrupoList(ListView):
    model = Group
    template_name = 'administracion/grupo_list.html'


class GrupoDetail(DetailView):
    model = Group
    template_name = 'administracion/grupo_detail.html'


class GrupoCreate(SuccessMessageMixin, CreateView):
    model = Group
    template_name = 'administracion/grupo_form.html'
    form_class = GroupForm
    success_url = reverse_lazy('administracion:grupo')
    success_message = "El grupo '%(name)s' fue creado con éxito"


class GrupoUpdate(SuccessMessageMixin, UpdateView):
    model = Group
    template_name = 'administracion/grupo_form.html'
    form_class = GroupForm
    success_url = reverse_lazy('administracion:grupo')
    success_message = "El grupo '%(name)s' fue modificado con éxito"


class GrupoDelete(SuccessMessageMixin, DeleteView):
    model = Group
    template_name = 'administracion/grupo_delete.html'
    success_url = reverse_lazy('administracion:grupo')
    success_message = "El grupo '%(name)s' fue eliminado con éxito"

    def delete(self, request, *args, **kwargs):
        messages.success(
            request, 'El grupo fue eliminado con éxito"')
        return super(GrupoDelete, self).delete(
            request, *args, **kwargs)
