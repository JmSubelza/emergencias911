from django.conf.urls import url
from apps.administracion.views import UsuarioCreate, GrupoCreate, GrupoList, UsuarioList


urlpatterns = [

    url(r'^usuario/$', UsuarioList.as_view(), name='usuario'),
    url(r'^usuario/nuevo/$', UsuarioCreate.as_view(), name='usuario_crear'),

    url(r'^grupo/$', GrupoList.as_view(), name='grupo'),
    url(r'^grupo/nuevo/$', GrupoCreate.as_view(), name='grupo_crear'),
]