# encoding:utf-8
from datetime import datetime
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Incidente, TipoIncidente, AsignacionIncidente
from .models import CentroEmergencia, Vehiculo
from .forms import IncidenteForm, TipoIncidenteForm, AsignacionIncidenteForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect


class IncidenteCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Incidente
    form_class = IncidenteForm
    template_name = 'logistica/incidente_form.html'
    success_url = reverse_lazy('logistica:incidente')
    success_message = "El incidente fue creado con éxito"
    permission_required = 'logistica.add_incidente'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('logistica:incidente')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IncidenteCreate, self).form_valid(form)


class IncidenteList(LoginRequiredMixin, ListView):
    model = Incidente
    template_name = 'logistica/incidente_list.html'

    # permission_required = 'logistica.view_incidente'

    def get_context_data(self, **kwargs):
        # Retorna a fecha y hora atual al campo de text data_now
        context = super(IncidenteList, self).get_context_data(**kwargs)
        context['date_now'] = datetime.now()
        return context

    def get_queryset(self):
        # Filtra por fecha
        super(IncidenteList, self).get_queryset()
        c = Incidente.objects.all()

        if self.request.GET.get('is_active') == '1':
            c = c.filter(is_active=True)
        elif self.request.GET.get('is_active') == '0':
            c = c.filter(is_active=False)

        q = self.request.GET.get('min_date')
        if not q in [None, '']:
            dmin = self.request.GET.get('min_date')
            dmax = self.request.GET.get('max_date')
            min_date = datetime.strptime(dmin, "%d/%m/%Y")
            max_date = datetime.strptime(dmax, "%d/%m/%Y")
            c = c.filter(time__gte=min_date, time__lte=max_date)
            # c = c.filter(time__range=(min_date, max_date))
        return c


class IncidenteDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Incidente
    template_name = 'logistica/incidente_detail.html'
    permission_required = 'logistica.view_incidente'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('logistica:incidente')


class IncidenteUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Incidente
    form_class = IncidenteForm
    template_name = 'logistica/incidente_update.html'
    success_url = reverse_lazy('logistica:incidente')
    success_message = "El incidente fue modificado con éxito"
    permission_required = 'logistica.change_incidente'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('logistica:incidente')


class IncidenteDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Incidente
    template_name = 'logistica/incidente_delete.html'
    success_url = reverse_lazy('logistica:incidente')
    success_message = "El incidente fue eliminado con éxito"
    permission_required = 'logistica.delete_incidente'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('logistica:incidente')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(IncidenteDelete, self).delete(request, *args, **kwargs)


class TipoIncidenteCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = TipoIncidente
    form_class = TipoIncidenteForm
    template_name = 'logistica/tipo_incidente_form.html'
    success_url = reverse_lazy('logistica:tipo_incidente')
    success_message = "El tipo de incidente (%(name)s) fue creado con éxito"
    permission_required = 'logistica.add_tipoincidente'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('logistica:tipo_incidente')


class TipoIncidenteUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TipoIncidente
    form_class = TipoIncidenteForm
    template_name = 'logistica/tipo_incidente_form.html'
    success_url = reverse_lazy('logistica:tipo_incidente')
    success_message = "El tipo de incidente (%(name)s) fue modificado con éxito"
    permission_required = 'logistica.change_tipoincidente'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('logistica:tipo_incidente')


class TipoIncidenteList(LoginRequiredMixin, ListView):
    model = TipoIncidente
    template_name = 'logistica/tipo_incidente_list.html'

    # permission_required = 'logistica.view_tipoincidente'

    def get_queryset(self):
        # Filtra por activo o inactivo
        super(TipoIncidenteList, self).get_queryset()
        c = TipoIncidente.objects.all()

        if self.request.GET.get('is_active') == '1':
            c = c.filter(is_active=True)
        elif self.request.GET.get('is_active') == '0':
            c = c.filter(is_active=False)
        return c


class TipoIncidenteDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = TipoIncidente
    template_name = 'logistica/tipo_incidente_detail.html'
    permission_required = 'logistica.view_tipoincidente'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('logistica:tipo_incidente')


class TipoIncidenteDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TipoIncidente
    template_name = 'logistica/tipo_incidente_delete.html'
    success_url = reverse_lazy('logistica:tipo_incidente')
    success_message = "El tipo de incidente (%(name)s) fue eliminado con éxito"
    permission_required = 'logistica.delete_tipoincidente'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('logistica:tipo_incidente')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(TipoIncidenteDelete, self).delete(request, *args, **kwargs)


class AsignacionIncidenteCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = AsignacionIncidente
    form_class = AsignacionIncidenteForm
    template_name = 'logistica/asignacion_incidente_form.html'
    success_url = reverse_lazy('logistica:asignacion_incidente')
    success_message = "La asignación fue creada con éxito"
    permission_required = 'logistica.add_asignacionincidente'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('logistica:asignacion_incidente')


class AsignacionIncidenteDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = AsignacionIncidente
    template_name = 'logistica/asignacion_incidente_detail.html'
    permission_required = 'logistica.view_asignacionincidente'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('logistica:asignacion_incidente')


class AsignacionIncidenteList(LoginRequiredMixin, ListView):
    model = AsignacionIncidente
    template_name = 'logistica/asignacion_incidente_list.html'

    # permission_required = 'logistica.view_asignacionincidente'

    def get_context_data(self, **kwargs):
        # Retorna a data atual
        context = super(AsignacionIncidenteList, self).get_context_data(**kwargs)
        context['date_now'] = datetime.now()
        return context

    def get_queryset(self):
        # Filtra por activo o inactivo
        super(AsignacionIncidenteList, self).get_queryset()
        c = AsignacionIncidente.objects.all()

        if self.request.GET.get('is_active') == '1':
            c = c.filter(is_active=True)
        elif self.request.GET.get('is_active') == '0':
            c = c.filter(is_active=False)
        # Filtra por fechas
        q = self.request.GET.get('min_date')
        if not q in [None, '']:
            dmin = self.request.GET.get('min_date')
            dmax = self.request.GET.get('max_date')
            min_date = datetime.strptime(dmin, "%d/%m/%Y")
            max_date = datetime.strptime(dmax, "%d/%m/%Y")
            c = c.filter(time__gte=min_date, time__lte=max_date)
            # c = c.filter(time__range=(min_date, max_date))

        return c


class AsignacionIncidenteUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AsignacionIncidente
    form_class = AsignacionIncidenteForm
    template_name = 'logistica/asignacion_incidente_form.html'
    success_url = reverse_lazy('logistica:asignacion_incidente')
    success_message = "La asignación fue modificada con éxito"
    permission_required = 'logistica.change_asignacionincidente'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('logistica:asignacion_incidente')


class AsignacionIncidenteDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = AsignacionIncidente
    template_name = 'logistica/asignacion_incidente_delete.html'
    success_url = reverse_lazy('logistica:asignacion_incidente')
    success_message = "La asignación fue eliminada con éxito"
    permission_required = 'logistica.delete_asignacionincidente'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('logistica:asignacion_incidente')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(AsignacionIncidenteDelete, self).delete(request, *args, **kwargs)


class MapaIncidente(LoginRequiredMixin, ListView):
    model = Incidente
    template_name = 'logistica/mapa_incidente.html'


class MapaCentroEmergencia(LoginRequiredMixin, ListView):
    model = CentroEmergencia
    template_name = 'logistica/mapa_centroemergencia.html'


class MapaVehiculo(LoginRequiredMixin, ListView):
    model = Vehiculo
    template_name = 'logistica/mapa_vehiculo.html'
