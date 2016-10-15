from django.conf.urls import url
from apps.logistica.views import \
    IncidenteCreate, IncidenteList

urlpatterns = [

    url(r'^incidente$', IncidenteList.as_view(), name='incidente'),
    url(r'^incidente/nuevo/$', IncidenteCreate.as_view(), name='inicidente_crear'),

    ]