from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.logistica.models import Incidente
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.administracion.forms import UserForm, GroupForm


# Create your views here.


class ReportIncidente(ListView):
    model = Incidente
