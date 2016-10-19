from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.logistica.models import Incidente, TipoIncidente, AsignacionIncidente
from apps.logistica.forms import IncidenteForm, TipoIncidenteForm, AsignacionIncidenteForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


# Create your views here.

class IncidenteCreate(CreateView):
    model = Incidente
    form_class = IncidenteForm
    template_name = 'logistica/incidente_form.html'
    success_url = reverse_lazy('logistica:incidente')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncidenteList(ListView):
    model = Incidente
    template_name = 'logistica/incidente_list.html'


class IncidenteUpdate(UpdateView):
    model = Incidente
    form_class = IncidenteForm
    template_name = 'logistica/incidente_form.html'
    success_url = reverse_lazy('logistica:incidente')


class IncidenteDelete(DeleteView):
    model = Incidente
    template_name = 'logistica/incidente_delete.html'
    success_url = reverse_lazy('logistica:incidente')


class TipoIncidenteCreate(CreateView):
    model = TipoIncidente
    form_class = TipoIncidenteForm
    template_name = 'logistica/tipo_incidente_form.html'
    success_url = reverse_lazy('logistica:tipo_incidente')


class TipoIncidenteUpdate(UpdateView):
    model = TipoIncidente
    form_class = TipoIncidenteForm
    template_name = 'logistica/tipo_incidente_form.html'
    success_url = reverse_lazy('logistica:tipo_incidente')


class TipoIncidenteList(ListView):
    model = TipoIncidente
    template_name = 'logistica/tipo_incidente_list.html'


class TipoIncidenteDelete(DeleteView):
    model = TipoIncidente
    template_name = 'logistica/tipo_incidente_delete.html'
    success_url = reverse_lazy('logistica:tipo_incidente')


class AsignacionIncidenteCreate(CreateView):
    model = AsignacionIncidente
    form_class = AsignacionIncidenteForm
    template_name = 'logistica/asignacion_incidente_form.html'
    success_url = reverse_lazy('logistica:asignacion_incidente')


class AsignacionIncidenteList(ListView):
    model = AsignacionIncidente
    template_name = 'logistica/asignacion_incidente_list.html'


class AsignacionIncidenteUpdate(UpdateView):
    model = AsignacionIncidente
    form_class = AsignacionIncidenteForm
    template_name = 'logistica/asignacion_incidente_form.html'
    success_url = reverse_lazy('logistica:asignacion_incidente')


class AsignacionIncidenteDelete(DeleteView):
    model = AsignacionIncidente
    template_name = 'logistica/asignacion_incidente_delete.html'
    success_url = reverse_lazy('logistica:asignacion_incidente')
