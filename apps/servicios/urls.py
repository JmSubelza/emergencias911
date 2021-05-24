from django.conf.urls import url
from django.urls import path
from .views import \
    VehiculoList, VehiculoCreate, VehiculoUpdate, VehiculoDelete, VehiculoDetail, TipoVehiculoList, TipoVehiculoCreate, \
    TipoVehiculoUpdate, TipoVehiculoDelete, TipoVehiculoDetail, CentroEmergernciaList, CentroEmergenciaCreate, \
    CentroEmergenciaUpdate, CentroEmergenciaDelete, CentroEmergenciaDetail, TipoCentroEmergenciaList, \
    TipoCentroEmergenciaCreate, TipoCentroEmergenciaUpdate, TipoCentroEmergenciaDelete, TipoCentroEmergenciaDetail

app_name = 'servicios'

urlpatterns = [
    path('vehiculo/', VehiculoList.as_view(), name='vehiculo'),
    path('vehiculo/nuevo/', VehiculoCreate.as_view(), name='vehiculo_crear'),
    path('vehiculo/editar/<int:pk>/', VehiculoUpdate.as_view(), name='vehiculo_editar'),
    path('vehiculo/delete/<int:pk>/', VehiculoDelete.as_view(), name='vehiculo_eliminar'),
    path('vehiculo/view/<int:pk>/', VehiculoDetail.as_view(), name='vehiculo_detalle'),

    path('tipovehiculo/', TipoVehiculoList.as_view(), name='tipo_vehiculo'),
    path('tipovehiculo/nuevo/', TipoVehiculoCreate.as_view(), name='tipo_vehiculo_crear'),
    path('tipovehiculo/editar/<int:pk>/', TipoVehiculoUpdate.as_view(), name='tipo_vehiculo_editar'),
    path('tipovehiculo/delete/<int:pk>/', TipoVehiculoDelete.as_view(), name='tipo_vehiculo_eliminar'),
    path('tipovehiculo/view/<int:pk>/', TipoVehiculoDetail.as_view(), name='tipo_vehiculo_detalle'),

    path('centroemergencia/', CentroEmergernciaList.as_view(), name='centro_emergencia'),
    path('centroemergencia/nuevo/', CentroEmergenciaCreate.as_view(), name='centro_emergencia_crear'),
    path('centroemergencia/editar/<int:pk>/', CentroEmergenciaUpdate.as_view(), name='centro_emergencia_editar'),
    path('centroemergencia/delete/<int:pk>/', CentroEmergenciaDelete.as_view(), name='centro_emergencia_eliminar'),
    path('centroemergencia/view/<int:pk>/', CentroEmergenciaDetail.as_view(), name='centro_emergencia_detalle'),

    path('tipocentroemergencia/', TipoCentroEmergenciaList.as_view(), name='tipo_centro_emergencia'),
    path('tipocentroemergencia/nuevo/', TipoCentroEmergenciaCreate.as_view(), name='tipo_centro_emergencia_crear'),
    path('tipocentroemergencia/editar/<int:pk>/', TipoCentroEmergenciaUpdate.as_view(),
         name='tipo_centro_emergencia_editar'),
    path('tipocentroemergencia/delete/<int:pk>/', TipoCentroEmergenciaDelete.as_view(),
         name='tipo_centro_emergencia_eliminar'),
    path('tipocentroemergencia/view/<int:pk>/', TipoCentroEmergenciaDetail.as_view(),
         name='tipo_centro_emergencia_detalle'),

]
