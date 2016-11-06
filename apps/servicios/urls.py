from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from apps.servicios.views import \
    VehiculoList, VehiculoCreate, VehiculoUpdate, VehiculoDelete, \
    TipoVehiculoList, TipoVehiculoCreate, TipoVehiculoUpdate, TipoVehiculoDelete, TipoVehiculoDetail, \
    CentroEmergernciaList, CentroEmergenciaCreate, CentroEmergenciaUpdate, CentroEmergenciaDelete, \
    DispositivoGpsList, DispositivoGpsCreate, DispositivoGpsUpdate, DispositivoGpsDelete

urlpatterns = [
    url(r'^vehiculo/$', VehiculoList.as_view(), name='vehiculo'),
    url(r'^vehiculo/nuevo/$', VehiculoCreate.as_view(), name='vehiculo_crear'),
    url(r'^vehiculo/editar/(?P<pk>\d+)/$', VehiculoUpdate.as_view(), name='vehiculo_editar'),
    url(r'^vehiculo/eliminar/(?P<pk>\d+)/$', VehiculoDelete.as_view(), name='vehiculo_eliminar'),

    url(r'^tipovehiculo/$', TipoVehiculoList.as_view(), name='tipo_vehiculo'),
    url(r'^tipovehiculo/nuevo/$', TipoVehiculoCreate.as_view(), name='tipo_vehiculo_crear'),
    url(r'^tipovehiculo/editar/(?P<pk>\d+)/$', TipoVehiculoUpdate.as_view(), name='tipo_vehiculo_editar'),
    url(r'^tipovehiculo/eliminar/(?P<pk>\d+)/$', TipoVehiculoDelete.as_view(), name='tipo_vehiculo_eliminar'),
    url(r'^tipovehiculo/detalle/(?P<pk>\d+)/$', TipoVehiculoDetail.as_view(), name='tipo_vehiculo_detalle'),

    url(r'^centroemergencia/$', CentroEmergernciaList.as_view(), name='centro_emergencia'),
    url(r'^centroemergencia/nuevo/$', CentroEmergenciaCreate.as_view(), name='centro_emergencia_crear'),
    url(r'^centroemergencia/editar/(?P<pk>\d+)/$', CentroEmergenciaUpdate.as_view(), name='centro_emergencia_editar'),
    url(r'^centroemergencia/eliminar/(?P<pk>\d+)/$', CentroEmergenciaDelete.as_view(),
        name='centro_emergencia_eliminar'),

    url(r'^dispositivogps/$', DispositivoGpsList.as_view(), name='dispositivo_gps'),
    url(r'^dispositivogps/nuevo/$', DispositivoGpsCreate.as_view(), name='dispositivo_gps_crear'),
    url(r'^dispositivogps/editar/(?P<pk>\d+)/$', DispositivoGpsUpdate.as_view(), name='dispositivo_gps_editar'),
    url(r'^dispositivogps/eliminar/(?P<pk>\d+)/$', DispositivoGpsDelete.as_view(), name='dispositivo_gps_eliminar'),

]
