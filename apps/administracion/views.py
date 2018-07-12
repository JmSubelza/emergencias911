# encoding:utf-8
from django.contrib.auth.models import User, Group
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm, GroupForm
from django.contrib import messages
from django.shortcuts import redirect


class UsuarioList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'administracion/usuario_list.html'

    # permission_required = 'auth.view_user'

    def get_queryset(self):
        # Filtra por activo o inactivo
        super(UsuarioList, self).get_queryset()
        c = User.objects.all()

        if self.request.GET.get('is_active') == '1':
            c = c.filter(is_active=True)
        elif self.request.GET.get('is_active') == '0':
            c = c.filter(is_active=False)
        return c


class UsuarioDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = User
    template_name = 'administracion/user_detail.html'
    permission_required = 'auth.view_user'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('administracion:usuario')


class UsuarioCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = User
    template_name = 'administracion/usuario_form.html'
    form_class = UserForm
    success_url = reverse_lazy('administracion:usuario')
    success_message = "El usuario (%(username)s) fue creado con éxito"
    permission_required = 'auth.add_user'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('administracion:usuario')

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


class UsuarioUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'administracion/usuario_form.html'
    form_class = UserForm
    success_url = reverse_lazy('administracion:usuario')
    success_message = "El usuario (%(username)s) fue modificado con éxito"
    permission_required = 'auth.change_user'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('administracion:usuario')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(form.cleaned_data['password'])
        obj.save()
        return super(UsuarioUpdate, self).form_valid(form)


class UsuarioDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'administracion/usuario_delete.html'
    success_url = reverse_lazy('administracion:usuario')
    success_message = "El usuario (%(username)s) fue eliminado con éxito"
    permission_required = 'auth.delete_user'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('administracion:usuario')

    def delete(self, request, *args, **kwargs):
        messages.success(
            request, 'El usuario fue eliminado')
        return super(UsuarioDelete, self).delete(
            request, *args, **kwargs)


class GrupoList(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'administracion/grupo_list.html'

    # permission_required = 'auth.view_group'


class GrupoDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Group
    template_name = 'administracion/grupo_detail.html'
    permission_required = 'auth.view_group'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('administracion:grupo')


class GrupoCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Group
    template_name = 'administracion/grupo_form.html'
    form_class = GroupForm
    success_url = reverse_lazy('administracion:grupo')
    success_message = "El grupo (%(name)s) fue creado con éxito"
    # group_required = 'Operador'
    permission_required = 'auth.add_group'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('administracion:grupo')


class GrupoUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Group
    template_name = 'administracion/grupo_form.html'
    form_class = GroupForm
    success_url = reverse_lazy('administracion:grupo')
    success_message = "El grupo (%(name)s) fue modificado con éxito"
    permission_required = 'auth.change_group'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('administracion:grupo')


class GrupoDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Group
    template_name = 'administracion/grupo_delete.html'
    success_url = reverse_lazy('administracion:grupo')
    success_message = "El grupo (%(name)s) fue eliminado con éxito"
    permission_required = 'auth.delete_group'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('administracion:grupo')

    def delete(self, request, *args, **kwargs):
        messages.success(
            request, 'El grupo fue eliminado con éxito')
        return super(GrupoDelete, self).delete(
            request, *args, **kwargs)
