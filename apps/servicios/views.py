from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from apps.servicios.forms import VehiculoForm, TipoVehiculoForm, CentroEmergenciaForm, DispositivoGpsForm
from apps.servicios.models import Vehiculo, TipoVehiculo, CentroEmergencia, DispositivoGPS
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


def index(request):
    return render(request, 'index.html')


def vehiculo_view(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('servicios:vehiculo')
    else:
        form = VehiculoForm()
    return render(request, 'servicios/vehiculo_form.html', {'form': form})


def vehiculo_list(request):
    vehiculo = Vehiculo.objects.all().order_by('placa')
    contexto = {'vehiculos': vehiculo}
    return render(request, 'servicios/vehiculo_list.html', contexto)


def vehiculo_edit(request, id_vehiculo):
    vehiculo = Vehiculo.objects.get(placa=id_vehiculo)
    if request.method == 'GET':
        form = VehiculoForm(instance=vehiculo)
    else:
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
        return redirect('servicios:vehiculo')
    return render(request, 'servicios/vehiculo_form.html', {'form': form})


def vehiculo_delete(request, id_vehiculo):
    vehiculo = Vehiculo.objects.get(placa=id_vehiculo)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('servicios:vehiculo')
    return render(request, 'servicios/vehiculo_delete.html', {'vehiculo': vehiculo})


class VehiculoList(ListView):
    model = Vehiculo
    template_name = 'servicios/vehiculo_list.html'


class VehiculoCreate(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'servicios/vehiculo_form.html'
    success_url = reverse_lazy('servicios:vehiculo')


class VehiculoUpdate(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'servicios/vehiculo_form.html'
    success_url = reverse_lazy('servicios:vehiculo')


class VehiculoDelete(DeleteView):
    model = Vehiculo
    template_name = 'servicios/vehiculo_delete.html'
    success_url = reverse_lazy('servicios:vehiculo')


class TipoVehiculoList(ListView):
    model = TipoVehiculo
    template_name = 'servicios/tipo_vehiculo_list.html'

    def get_queryset(self):
        queryset = super(TipoVehiculoList, self).get_queryset()
        if self.request.GET.get("descripcion"):
            selection = self.request.GET.get("descripcion")
            return queryset.filter(name__icontains=selection)
        else:
            return TipoVehiculo.objects.all()


class TipoVehiculoCreate(CreateView):
    model = TipoVehiculo
    form_class = TipoVehiculoForm
    template_name = 'servicios/tipo_vehiculo_form.html'
    success_url = reverse_lazy('servicios:tipo_vehiculo')


class TipoVehiculoUpdate(UpdateView):
    model = TipoVehiculo
    form_class = TipoVehiculoForm
    template_name = 'servicios/tipo_vehiculo_form.html'
    success_url = reverse_lazy('servicios:tipo_vehiculo')


class TipoVehiculoDelete(DeleteView):
    model = TipoVehiculo
    template_name = 'servicios/tipo_vehiculo_delete.html'
    success_url = reverse_lazy('servicios:tipo_vehiculo')


class CentroEmergernciaList(ListView):
    model = CentroEmergencia
    template_name = 'servicios/centro_emergencia_list.html'


class CentroEmergenciaCreate(CreateView):
    model = CentroEmergencia
    form_class = CentroEmergenciaForm
    template_name = 'servicios/centro_emergencia_form.html'
    success_url = reverse_lazy('servicios:centro_emergencia')


class CentroEmergenciaUpdate(UpdateView):
    model = CentroEmergencia
    form_class = CentroEmergenciaForm
    template_name = 'servicios/centro_emergencia_update.html'
    success_url = reverse_lazy('servicios:centro_emergencia')


class CentroEmergenciaDelete(DeleteView):
    model = CentroEmergencia
    template_name = 'servicios/centro_emergencia_delete.html'
    success_url = reverse_lazy('servicios:centro_emergencia')


class DispositivoGpsList(ListView):
    model = DispositivoGPS
    template_name = 'servicios/dispositivi_gps_list.html'


class DispositivoGpsCreate(CreateView):
    model = DispositivoGPS
    form_class = DispositivoGpsForm
    template_name = 'servicios/dispositivo_gps_form.html'
    success_url = reverse_lazy('servicios:dispositivo_gps')


class DispositivoGpsUpdate(UpdateView):
    model = DispositivoGPS
    form_class = DispositivoGpsForm
    template_name = 'servicios/dispositivo_gps_form.html'
    success_url = reverse_lazy('servicios:dispositivo_gps')


class DispositivoGpsDelete(DeleteView):
    model = DispositivoGPS
    template_name = 'servicios/dispositivo_gps_delete.html'
    success_url = reverse_lazy('servicios:dispositivo_gps')
