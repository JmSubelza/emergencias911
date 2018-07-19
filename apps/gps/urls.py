from django.conf.urls import url
from .views import \
    DispositivoGpsList, DispositivoGpsCreate, DispositivoGpsUpdate, DispositivoGpsDelete, DispositivoGpsDetail

urlpatterns = [
    url(r'^dispositivogps/$', DispositivoGpsList.as_view(), name='dispositivo_gps'),
    url(r'^dispositivogps/nuevo/$', DispositivoGpsCreate.as_view(), name='dispositivo_gps_crear'),
    url(r'^dispositivogps/editar/(?P<pk>\d+)/$', DispositivoGpsUpdate.as_view(),
        name='dispositivo_gps_editar'),
    url(r'^dispositivogps/delete/(?P<pk>\d+)/$', DispositivoGpsDelete.as_view(),
        name='dispositivo_gps_eliminar'),
    url(r'^dispositivogps/view/(?P<pk>\d+)/$', DispositivoGpsDetail.as_view(),
        name='dispositivo_gps_detalle'),

]
