from django.conf.urls import url
from apps.servicios.views import index, vehiculo_view, vehiculo_list, vehiculo_edit, vehiculo_delete, \
    VehiculoList, VehiculoCreate, VehiculoUpdate, VehiculoDelete, \
    TipoVehiculoList, TipoVehiculoCreate, TipoVehiculoUpdate, TipoVehiculoDelete

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^vehiculo$', VehiculoList.as_view(), name='vehiculo'),
    url(r'^vehiculo/nuevo$', VehiculoCreate.as_view(), name='vehiculo_crear'),
    url(r'^vehiculo/editar/(?P<pk>\d+)/$', VehiculoUpdate.as_view(), name='vehiculo_editar'),
    url(r'^vehiculo/eliminar/(?P<pk>\d+)/$', VehiculoDelete.as_view(), name='vehiculo_eliminar'),

    url(r'^tipovehiculo$', TipoVehiculoList.as_view(), name='tipo_vehiculo'),
    url(r'^tipovehiculo/nuevo$', TipoVehiculoCreate.as_view(), name='tipo_vehiculo_crear'),
    url(r'^tipovehiculo/editar/(?P<pk>\d+)/$', TipoVehiculoUpdate.as_view(), name='tipo_vehiculo_editar'),
    url(r'^tipovehiculo/eliminar/(?P<pk>\d+)/$', TipoVehiculoDelete.as_view(), name='tipo_vehiculo_eliminar'),
]