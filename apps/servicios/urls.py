from django.conf.urls import url
from apps.servicios.views import index, vehiculo_view, vehiculo_list, vehiculo_edit, vehiculo_delete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^vehiculo$', vehiculo_list, name='vehiculo'),
    url(r'^vehiculo/nuevo$', vehiculo_view, name='vehiculo_crear'),
    url(r'^vehiculo/editar/(?P<id_vehiculo>\w+)/$', vehiculo_edit, name='vehiculo_editar'),
    url(r'^vehiculo/eliminar/(?P<id_vehiculo>\w+)/$', vehiculo_delete, name='vehiculo_eliminar'),
]