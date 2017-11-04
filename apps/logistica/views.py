# encoding:utf-8
from datetime import datetime
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .models import Incidente, TipoIncidente, AsignacionIncidente
from .models import CentroEmergencia, Vehiculo
from .forms import IncidenteForm, TipoIncidenteForm, AsignacionIncidenteForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView


# Create your views here.

class IncidenteCreate(SuccessMessageMixin, CreateView):
    model = Incidente
    form_class = IncidenteForm
    template_name = 'logistica/incidente_form.html'
    success_url = reverse_lazy('logistica:incidente')
    success_message = "El incidente fue creado con éxito"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IncidenteCreate, self).form_valid(form)


class IncidenteList(ListView):
    model = Incidente
    template_name = 'logistica/incidente_list.html'

    def get_context_data(self, **kwargs):
        # Retorna a data atual
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


class IncidenteDetail(DetailView):
    model = Incidente
    template_name = 'logistica/incidente_detail.html'


class IncidenteUpdate(SuccessMessageMixin, UpdateView):
    model = Incidente
    form_class = IncidenteForm
    template_name = 'logistica/incidente_update.html'
    success_url = reverse_lazy('logistica:incidente')
    success_message = "El incidente fue modificado con éxito"


class IncidenteDelete(DeleteView):
    model = Incidente
    template_name = 'logistica/incidente_delete.html'
    success_url = reverse_lazy('logistica:incidente')

    def delete(self, request, *args, **kwargs):
        messages.success(
            request, 'El incidente fue eliminado')
        return super(IncidenteDelete, self).delete(
            request, *args, **kwargs)


class TipoIncidenteCreate(SuccessMessageMixin, CreateView):
    model = TipoIncidente
    form_class = TipoIncidenteForm
    template_name = 'logistica/tipo_incidente_form.html'
    success_url = reverse_lazy('logistica:tipo_incidente')
    success_message = "El tipo de incidente fue creado con éxito"


class TipoIncidenteUpdate(SuccessMessageMixin, UpdateView):
    model = TipoIncidente
    form_class = TipoIncidenteForm
    template_name = 'logistica/tipo_incidente_form.html'
    success_url = reverse_lazy('logistica:tipo_incidente')
    success_message = "El tipo de incidente fue modificado con éxito"


class TipoIncidenteList(ListView):
    model = TipoIncidente
    template_name = 'logistica/tipo_incidente_list.html'

    def get_queryset(self):
        # Filtra por activo o inactivo
        super(TipoIncidenteList, self).get_queryset()
        c = TipoIncidente.objects.all()

        if self.request.GET.get('is_active') == '1':
            c = c.filter(is_active=True)
        elif self.request.GET.get('is_active') == '0':
            c = c.filter(is_active=False)
        return c


class TipoIncidenteDetail(DetailView):
    model = TipoIncidente
    template_name = 'logistica/tipo_incidente_detail.html'


class TipoIncidenteDelete(DeleteView):
    model = TipoIncidente
    template_name = 'logistica/tipo_incidente_delete.html'
    success_url = reverse_lazy('logistica:tipo_incidente')

    def delete(self, request, *args, **kwargs):
        messages.success(
            request, 'El tipo de incidente fue eliminado')
        return super(TipoIncidenteDelete, self).delete(
            request, *args, **kwargs)


class AsignacionIncidenteCreate(SuccessMessageMixin, CreateView):
    model = AsignacionIncidente
    form_class = AsignacionIncidenteForm
    template_name = 'logistica/asignacion_incidente_form.html'
    success_url = reverse_lazy('logistica:asignacion_incidente')
    success_message = "La asignación fue creada con éxito"


class AsignacionIncidenteDetail(DetailView):
    model = AsignacionIncidente
    template_name = 'logistica/asignacion_incidente_detail.html'


class AsignacionIncidenteList(ListView):
    model = AsignacionIncidente
    template_name = 'logistica/asignacion_incidente_list.html'

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


class AsignacionIncidenteUpdate(SuccessMessageMixin, UpdateView):
    model = AsignacionIncidente
    form_class = AsignacionIncidenteForm
    template_name = 'logistica/asignacion_incidente_form.html'
    success_url = reverse_lazy('logistica:asignacion_incidente')
    success_message = "La asignación fue modificada con éxito"


class AsignacionIncidenteDelete(DeleteView):
    model = AsignacionIncidente
    template_name = 'logistica/asignacion_incidente_delete.html'
    success_url = reverse_lazy('logistica:asignacion_incidente')

    def delete(self, request, *args, **kwargs):
        messages.success(
            request, 'La asignacion del incidente fue eliminado')
        return super(AsignacionIncidenteDelete, self).delete(
            request, *args, **kwargs)


class MapaIncidente(ListView):
    model = Incidente
    template_name = 'logistica/mapa_incidente.html'


class MapaCentroEmergencia(ListView):
    model = CentroEmergencia
    template_name = 'logistica/mapa_centroemergencia.html'


class MapaVehiculo(ListView):
    model = Vehiculo
    template_name = 'logistica/mapa_vehiculo.html'
