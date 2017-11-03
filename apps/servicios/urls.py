from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import \
    VehiculoList, VehiculoCreate, VehiculoUpdate, VehiculoDelete, VehiculoDetail, TipoVehiculoList, TipoVehiculoCreate, \
    TipoVehiculoUpdate, TipoVehiculoDelete, TipoVehiculoDetail, CentroEmergernciaList, CentroEmergenciaCreate, \
    CentroEmergenciaUpdate, CentroEmergenciaDelete, CentroEmergenciaDetail, DispositivoGpsList, DispositivoGpsCreate, \
    DispositivoGpsUpdate, DispositivoGpsDelete, DispositivoGpsDetail

urlpatterns = [
    url(r'^vehiculo/$', login_required(VehiculoList.as_view()), name='vehiculo'),
    url(r'^vehiculo/nuevo/$', login_required(VehiculoCreate.as_view()), name='vehiculo_crear'),
    url(r'^vehiculo/editar/(?P<pk>\d+)/$', login_required(VehiculoUpdate.as_view()), name='vehiculo_editar'),
    url(r'^vehiculo/eliminar/(?P<pk>\d+)/$', login_required(VehiculoDelete.as_view()), name='vehiculo_eliminar'),
    url(r'^vehiculo/detalle/(?P<pk>\d+)/$', login_required(VehiculoDetail.as_view()), name='vehiculo_detalle'),

    url(r'^tipovehiculo/$', login_required(TipoVehiculoList.as_view()), name='tipo_vehiculo'),
    url(r'^tipovehiculo/nuevo/$', login_required(TipoVehiculoCreate.as_view()), name='tipo_vehiculo_crear'),
    url(r'^tipovehiculo/editar/(?P<pk>\d+)/$', login_required(TipoVehiculoUpdate.as_view()), name='tipo_vehiculo_editar'),
    url(r'^tipovehiculo/eliminar/(?P<pk>\d+)/$', login_required(TipoVehiculoDelete.as_view()), name='tipo_vehiculo_eliminar'),
    url(r'^tipovehiculo/detalle/(?P<pk>\d+)/$', login_required(TipoVehiculoDetail.as_view()), name='tipo_vehiculo_detalle'),

    url(r'^centroemergencia/$', login_required(CentroEmergernciaList.as_view()), name='centro_emergencia'),
    url(r'^centroemergencia/nuevo/$', login_required(CentroEmergenciaCreate.as_view()), name='centro_emergencia_crear'),
    url(r'^centroemergencia/editar/(?P<pk>\d+)/$', login_required(CentroEmergenciaUpdate.as_view()), name='centro_emergencia_editar'),
    url(r'^centroemergencia/eliminar/(?P<pk>\d+)/$', login_required(CentroEmergenciaDelete.as_view()),
        name='centro_emergencia_eliminar'),
    url(r'^centroemergencia/detalle/(?P<pk>\d+)/$', login_required(CentroEmergenciaDetail.as_view()),
        name='centro_emergencia_detalle'),

    url(r'^dispositivogps/$', login_required(DispositivoGpsList.as_view()), name='dispositivo_gps'),
    url(r'^dispositivogps/nuevo/$', login_required(DispositivoGpsCreate.as_view()), name='dispositivo_gps_crear'),
    url(r'^dispositivogps/editar/(?P<pk>\d+)/$', login_required(DispositivoGpsUpdate.as_view()), name='dispositivo_gps_editar'),
    url(r'^dispositivogps/eliminar/(?P<pk>\d+)/$', login_required(DispositivoGpsDelete.as_view()), name='dispositivo_gps_eliminar'),
    url(r'^dispositivogps/detalle/(?P<pk>\d+)/$', login_required(DispositivoGpsDetail.as_view()), name='dispositivo_gps_detalle'),

]
