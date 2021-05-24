from django.urls import reverse_lazy
from .forms import VehiculoForm, TipoVehiculoForm, CentroEmergenciaForm, TipoCentroEmergenciaForm
from .models import Vehiculo, TipoVehiculo, CentroEmergencia, TipoCentroEmergencia
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect


class VehiculoList(LoginRequiredMixin, ListView):
    model = Vehiculo
    template_name = 'servicios/vehiculo_list.html'

    # permission_required = 'servicios.view_vehiculo'

    def get_queryset(self):
        # Filtra por activo o inactivo
        super(VehiculoList, self).get_queryset()
        c = Vehiculo.objects.all()

        if self.request.GET.get('is_active') == '1':
            c = c.filter(is_active=True)
        elif self.request.GET.get('is_active') == '0':
            c = c.filter(is_active=False)
        elif self.request.GET.get('sector') == 'publico':
            c = c.filter(sector__contains='PUBLICO')
        elif self.request.GET.get('sector') == 'privado':
            c = c.filter(sector__contains='PRIVADO')
        return c


class VehiculoDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Vehiculo
    template_name = 'servicios/vehiculo_detail.html'
    permission_required = 'servicios.view_vehiculo'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:vehiculo')


class VehiculoCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'servicios/vehiculo_form.html'
    success_url = reverse_lazy('servicios:vehiculo')
    success_message = "El vehiculo con placa (%(placa)s) fue creado con éxito"
    permission_required = 'servicios.add_vehiculo'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:vehiculo')


class VehiculoUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'servicios/vehiculo_form.html'
    success_url = reverse_lazy('servicios:vehiculo')
    success_message = "El vehiculo con placa (%(placa)s) fue modificado con éxito"
    permission_required = 'servicios.change_vehiculo'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:vehiculo')


class VehiculoDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Vehiculo
    template_name = 'servicios/vehiculo_delete.html'
    success_url = reverse_lazy('servicios:vehiculo')
    success_message = "El vehiculo con placa (%(placa)s)fue eliminado con éxito"
    permission_required = 'servicios.delete_vehiculo'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:vehiculo')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(VehiculoDelete, self).delete(request, *args, **kwargs)


class TipoVehiculoList(LoginRequiredMixin, ListView):
    model = TipoVehiculo
    template_name = 'servicios/tipo_vehiculo_list.html'

    # permission_required = 'servicios.view_tipovehiculo'

    def get_queryset(self):
        # Filtra por activo o inactivo
        super(TipoVehiculoList, self).get_queryset()
        c = TipoVehiculo.objects.all()

        if self.request.GET.get('is_active') == '1':
            c = c.filter(is_active=True)
        elif self.request.GET.get('is_active') == '0':
            c = c.filter(is_active=False)
        return c


class TipoVehiculoCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = TipoVehiculo
    form_class = TipoVehiculoForm
    template_name = 'servicios/tipo_vehiculo_form.html'
    success_url = reverse_lazy('servicios:tipo_vehiculo')
    success_message = "El tipo de vehiculo (%(name)s) fue creado con éxito"
    permission_required = 'servicios.add_tipovehiculo'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:tipo_vehiculo')


class TipoVehiculoDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = TipoVehiculo
    template_name = 'servicios/tipo_vehiculo_detail.html'
    permission_required = 'servicios.view_tipovehiculo'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:tipo_vehiculo')


class TipoVehiculoUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TipoVehiculo
    form_class = TipoVehiculoForm
    template_name = 'servicios/tipo_vehiculo_form.html'
    success_url = reverse_lazy('servicios:tipo_vehiculo')
    success_message = "El tipo de vehiculo (%(name)s) fue modificado con éxito"
    permission_required = 'servicios.change_tipovehiculo'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:tipo_vehiculo')


class TipoVehiculoDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TipoVehiculo
    template_name = 'servicios/tipo_vehiculo_delete.html'
    success_url = reverse_lazy('servicios:tipo_vehiculo')
    success_message = "El tipo de vehiculo (%(name)s) fue eliminado con éxito"
    permission_required = 'servicios.delete_tipovehiculo'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:tipo_vehiculo')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(TipoVehiculoDelete, self).delete(request, *args, **kwargs)


class CentroEmergernciaList(LoginRequiredMixin, ListView):
    model = CentroEmergencia
    template_name = 'servicios/centro_emergencia_list.html'

    # permission_required = 'servicios.view_centroemergencia'

    def get_queryset(self):
        # Filtra por activo o inactivo
        super(CentroEmergernciaList, self).get_queryset()
        c = CentroEmergencia.objects.all()

        if self.request.GET.get('is_active') == '1':
            c = c.filter(is_active=True)
        elif self.request.GET.get('is_active') == '0':
            c = c.filter(is_active=False)
        elif self.request.GET.get('sector_tipo') == 'salud':
            c = c.filter(tipo__contains='SALUD')
        elif self.request.GET.get('sector_tipo') == 'seguridad':
            c = c.filter(tipo__contains='SEGURIDAD')
        elif self.request.GET.get('sector_tipo') == 'bomberos':
            c = c.filter(tipo__contains='BOMBEROS')
        elif self.request.GET.get('sector_tipo') == 'transito':
            c = c.filter(tipo__contains='TRANSITO')
        elif self.request.GET.get('sector_tipo') == 'publico':
            c = c.filter(sector__contains='PUBLICO')
        elif self.request.GET.get('sector_tipo') == 'privado':
            c = c.filter(sector__contains='PRIVADO')
        return c


class CentroEmergenciaDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = CentroEmergencia
    template_name = 'servicios/centro_emergencia_detail.html'
    permission_required = 'servicios.view_centroemergencia'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:centro_emergencia')


class CentroEmergenciaCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = CentroEmergencia
    form_class = CentroEmergenciaForm
    template_name = 'servicios/centro_emergencia_form.html'
    success_url = reverse_lazy('servicios:centro_emergencia')
    success_message = "El centro de emergencia (%(name)s) fue creado con éxito"
    permission_required = 'servicios.add_centroemergencia'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:centro_emergencia')


class CentroEmergenciaUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CentroEmergencia
    form_class = CentroEmergenciaForm
    template_name = 'servicios/centro_emergencia_update.html'
    success_url = reverse_lazy('servicios:centro_emergencia')
    success_message = "El centro de emergencia (%(name)s) fue modificado con éxito"
    permission_required = 'servicios.change_centroemergencia'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:centro_emergencia')


class CentroEmergenciaDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CentroEmergencia
    template_name = 'servicios/centro_emergencia_delete.html'
    success_url = reverse_lazy('servicios:centro_emergencia')
    success_message = "El centro de emergencia (%(name)s) fue eliminado con éxito"
    permission_required = 'servicios.delete_centroemergencia'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:centro_emergencia')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(CentroEmergenciaDelete, self).delete(request, *args, **kwargs)


class TipoCentroEmergenciaList(LoginRequiredMixin, ListView):
    model = TipoCentroEmergencia
    template_name = 'servicios/tipo_centro_emergencia_list.html'

    # permission_required = 'servicios.view_tipovehiculo'

    def get_queryset(self):
        # Filtra por activo o inactivo
        super(TipoCentroEmergenciaList, self).get_queryset()
        c = TipoCentroEmergencia.objects.all()

        if self.request.GET.get('is_active') == '1':
            c = c.filter(is_active=True)
        elif self.request.GET.get('is_active') == '0':
            c = c.filter(is_active=False)
        return c


class TipoCentroEmergenciaCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = TipoCentroEmergencia
    form_class = TipoCentroEmergenciaForm
    template_name = 'servicios/tipo_centro_emergencia_form.html'
    success_url = reverse_lazy('servicios:tipo_centro_emergencia')
    success_message = "El tipo de centro de emergencia (%(name)s) fue creado con éxito"
    permission_required = 'servicios.add_tipocentroemergencia'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:tipo_centro_emergencia')


class TipoCentroEmergenciaDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = TipoCentroEmergencia
    template_name = 'servicios/tipo_centro_emergencia_detail.html'
    permission_required = 'servicios.view_tipocentroemergencia'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:tipo_centro_emergencia')


class TipoCentroEmergenciaUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TipoCentroEmergencia
    form_class = TipoCentroEmergenciaForm
    template_name = 'servicios/tipo_centro_emergencia_form.html'
    success_url = reverse_lazy('servicios:tipo_centro_emergencia')
    success_message = "El tipo de centro de emergencia (%(name)s) fue modificado con éxito"
    permission_required = 'servicios.change_tipocentroemergencia'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:tipo_centro_emergencia')


class TipoCentroEmergenciaDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TipoCentroEmergencia
    template_name = 'servicios/tipo_centro_emergencia_delete.html'
    success_url = reverse_lazy('servicios:tipo_centro_emergencia')
    success_message = "El tipo de vehiculo (%(name)s) fue eliminado con éxito"
    permission_required = 'servicios.delete_tipocentroemergencia'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('servicios:tipo_centro_emergencia')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(TipoCentroEmergenciaDelete, self).delete(request, *args, **kwargs)
