from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.logistica.models import Incidente
from apps.logistica.forms import IncidenteForm
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