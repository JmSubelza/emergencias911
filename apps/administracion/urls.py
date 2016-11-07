from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from apps.administracion.views import \
    UsuarioList, UsuarioCreate, UsuarioUpdate, UsuarioDelete, UsuarioDetail, \
    GrupoCreate, GrupoList, GrupoUpdate, GrupoDelete, GrupoDetail

urlpatterns = [

    url(r'^usuario/$', login_required(UsuarioList.as_view()), name='usuario'),
    url(r'^usuario/nuevo/$', login_required(UsuarioCreate.as_view()), name='usuario_crear'),
    url(r'^usuario/editar/(?P<pk>\d+)/$', login_required(UsuarioUpdate.as_view()), name='usuario_editar'),
    url(r'^usuario/eliminar/(?P<pk>\d+)/$', login_required(UsuarioDelete.as_view()), name='usuario_eliminar'),
    url(r'^usuario/detalle/(?P<pk>\d+)/$', login_required(UsuarioDetail.as_view()), name='usuario_detalle'),


    url(r'^grupo/$', GrupoList.as_view(), name='grupo'),
    url(r'^grupo/nuevo/$', GrupoCreate.as_view(), name='grupo_crear'),
    url(r'^grupo/editar/(?P<pk>\d+)/$', GrupoUpdate.as_view(), name='grupo_editar'),
    url(r'^grupo/eliminar/(?P<pk>\d+)/$', GrupoDelete.as_view(), name='grupo_eliminar'),
    url(r'^grupo/detalle/(?P<pk>\d+)/$', GrupoDetail.as_view(), name='grupo_detalle'),

]
