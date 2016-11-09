from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.servicios.forms import VehiculoForm, TipoVehiculoForm, CentroEmergenciaForm, DispositivoGpsForm
from apps.servicios.models import Vehiculo, TipoVehiculo, CentroEmergencia, DispositivoGPS
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView


class VehiculoList(ListView):
    model = Vehiculo
    template_name = 'servicios/vehiculo_list.html'

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


class VehiculoDetail(DetailView):
    model = Vehiculo
    template_name = 'servicios/vehiculo_detail.html'


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
        # Filtra por activo o inactivo
        super(TipoVehiculoList, self).get_queryset()
        c = TipoVehiculo.objects.all()

        if self.request.GET.get('is_active') == '1':
            c = c.filter(is_active=True)
        elif self.request.GET.get('is_active') == '0':
            c = c.filter(is_active=False)
        return c


class TipoVehiculoCreate(CreateView):
    model = TipoVehiculo
    form_class = TipoVehiculoForm
    template_name = 'servicios/tipo_vehiculo_form.html'
    success_url = reverse_lazy('servicios:tipo_vehiculo')


class TipoVehiculoDetail(DetailView):
    model = TipoVehiculo
    template_name = 'servicios/tipo_vehiculo_detail.html'


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


class CentroEmergenciaDetail(DetailView):
    model = CentroEmergencia
    template_name = 'servicios/centro_emergencia_detail.html'


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

    def get_queryset(self):
        # Filtra por activo o inactivo
        super(DispositivoGpsList, self).get_queryset()
        c = DispositivoGPS.objects.all()

        if self.request.GET.get('is_active') == '1':
            c = c.filter(is_active=True)
        elif self.request.GET.get('is_active') == '0':
            c = c.filter(is_active=False)

        return c


class DispositivoGpsDetail(DetailView):
    model = DispositivoGPS
    template_name = 'servicios/dispositivo_gps_detail.html'


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
