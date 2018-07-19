from django.conf.urls import url
from .views import \
    VehiculoList, VehiculoCreate, VehiculoUpdate, VehiculoDelete, VehiculoDetail, TipoVehiculoList, TipoVehiculoCreate, \
    TipoVehiculoUpdate, TipoVehiculoDelete, TipoVehiculoDetail, CentroEmergernciaList, CentroEmergenciaCreate, \
    CentroEmergenciaUpdate, CentroEmergenciaDelete, CentroEmergenciaDetail, TipoCentroEmergenciaList, \
    TipoCentroEmergenciaCreate, TipoCentroEmergenciaUpdate, TipoCentroEmergenciaDelete, TipoCentroEmergenciaDetail

urlpatterns = [
    url(r'^vehiculo/$', VehiculoList.as_view(), name='vehiculo'),
    url(r'^vehiculo/nuevo/$', VehiculoCreate.as_view(), name='vehiculo_crear'),
    url(r'^vehiculo/editar/(?P<pk>\d+)/$', VehiculoUpdate.as_view(), name='vehiculo_editar'),
    url(r'^vehiculo/delete/(?P<pk>\d+)/$', VehiculoDelete.as_view(), name='vehiculo_eliminar'),
    url(r'^vehiculo/view/(?P<pk>\d+)/$', VehiculoDetail.as_view(),
        name='vehiculo_detalle'),

    url(r'^tipovehiculo/$', TipoVehiculoList.as_view(), name='tipo_vehiculo'),
    url(r'^tipovehiculo/nuevo/$', TipoVehiculoCreate.as_view(), name='tipo_vehiculo_crear'),
    url(r'^tipovehiculo/editar/(?P<pk>\d+)/$', TipoVehiculoUpdate.as_view(),
        name='tipo_vehiculo_editar'),
    url(r'^tipovehiculo/delete/(?P<pk>\d+)/$', TipoVehiculoDelete.as_view(),
        name='tipo_vehiculo_eliminar'),
    url(r'^tipovehiculo/view/(?P<pk>\d+)/$', TipoVehiculoDetail.as_view(),
        name='tipo_vehiculo_detalle'),

    url(r'^centroemergencia/$', CentroEmergernciaList.as_view(), name='centro_emergencia'),
    url(r'^centroemergencia/nuevo/$', CentroEmergenciaCreate.as_view(), name='centro_emergencia_crear'),
    url(r'^centroemergencia/editar/(?P<pk>\d+)/$', CentroEmergenciaUpdate.as_view(),
        name='centro_emergencia_editar'),
    url(r'^centroemergencia/delete/(?P<pk>\d+)/$', CentroEmergenciaDelete.as_view(),
        name='centro_emergencia_eliminar'),
    url(r'^centroemergencia/view/(?P<pk>\d+)/$', CentroEmergenciaDetail.as_view(),
        name='centro_emergencia_detalle'),

    url(r'^tipocentroemergencia/$', TipoCentroEmergenciaList.as_view(), name='tipo_centro_emergencia'),
    url(r'^tipocentroemergencia/nuevo/$', TipoCentroEmergenciaCreate.as_view(), name='tipo_centro_emergencia_crear'),
    url(r'^tipocentroemergencia/editar/(?P<pk>\d+)/$', TipoCentroEmergenciaUpdate.as_view(),
        name='tipo_centro_emergencia_editar'),
    url(r'^tipocentroemergencia/delete/(?P<pk>\d+)/$', TipoCentroEmergenciaDelete.as_view(),
        name='tipo_centro_emergencia_eliminar'),
    url(r'^tipocentroemergencia/view/(?P<pk>\d+)/$', TipoCentroEmergenciaDetail.as_view(),
        name='tipo_centro_emergencia_detalle'),

]
