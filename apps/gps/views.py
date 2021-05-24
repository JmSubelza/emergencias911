from django.urls import reverse_lazy
from .forms import DispositivoGpsForm
from .models import Device
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
class DispositivoGpsList(LoginRequiredMixin, ListView):
    model = Device
    template_name = 'gps/dispositivo_gps_list.html'

    # permission_required = 'servicios.view_dispositivogps'

    def get_queryset(self):
        # Filtra por activo o inactivo
        super(DispositivoGpsList, self).get_queryset()
        c = Device.objects.all()

        if self.request.GET.get('is_active') == '1':
            c = c.filter(is_active=True)
        elif self.request.GET.get('is_active') == '0':
            c = c.filter(is_active=False)

        return c


class DispositivoGpsDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Device
    template_name = 'gps/dispositivo_gps_detail.html'
    permission_required = 'gps.view_device'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('gps:dispositivo_gps')


class DispositivoGpsCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Device
    form_class = DispositivoGpsForm
    template_name = 'gps/dispositivo_gps_form.html'
    success_url = reverse_lazy('gps:dispositivo_gps')
    success_message = "El GPS con imei (%(imei)s) fue creado con éxito"
    permission_required = 'gps.add_device'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('gps:dispositivo_gps')


class DispositivoGpsUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Device
    form_class = DispositivoGpsForm
    template_name = 'gps/dispositivo_gps_form.html'
    success_url = reverse_lazy('gps:dispositivo_gps')
    success_message = "El GPS con imei (%(imei)s) fue modificado con éxito"
    permission_required = 'gps.change_device'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('gps:dispositivo_gps')


class DispositivoGpsDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Device
    template_name = 'gps/dispositivo_gps_delete.html'
    success_url = reverse_lazy('gps:dispositivo_gps')
    success_message = "El GPS con imei (%(imei)s) fue eliminado con éxito"
    permission_required = 'gps.delete_device'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para hacer esto')
        return redirect('gps:dispositivo_gps')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DispositivoGpsDelete, self).delete(request, *args, **kwargs)
