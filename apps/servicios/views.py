from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from apps.servicios.forms import VehiculoForm
from apps.servicios.models import Vehiculo


def index(request):
    return render(request, 'servicios/index.html')


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

