from django.conf.urls import url
from .views import \
    UsuarioList, UsuarioCreate, UsuarioUpdate, UsuarioDelete, UsuarioDetail, \
    GrupoCreate, GrupoList, GrupoUpdate, GrupoDelete, GrupoDetail

urlpatterns = [

    url(r'^usuario/$', UsuarioList.as_view(), name='usuario'),
    url(r'^usuario/nuevo/$', UsuarioCreate.as_view(), name='usuario_crear'),
    url(r'^usuario/editar/(?P<pk>\d+)/$', UsuarioUpdate.as_view(), name='usuario_editar'),
    url(r'^usuario/delete/(?P<pk>\d+)/$', UsuarioDelete.as_view(), name='usuario_eliminar'),
    url(r'^usuario/view/(?P<pk>\d+)/$', UsuarioDetail.as_view(), name='usuario_detalle'),

    url(r'^grupo/$', GrupoList.as_view(), name='grupo'),
    url(r'^grupo/nuevo/$', GrupoCreate.as_view(), name='grupo_crear'),
    url(r'^grupo/editar/(?P<pk>\d+)/$', GrupoUpdate.as_view(), name='grupo_editar'),
    url(r'^grupo/delete/(?P<pk>\d+)/$', GrupoDelete.as_view(), name='grupo_eliminar'),
    url(r'^grupo/view/(?P<pk>\d+)/$', GrupoDetail.as_view(), name='grupo_detalle'),

]
