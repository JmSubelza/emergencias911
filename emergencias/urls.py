"""emergencias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import reverse_lazy, path, include
from django.views.generic import RedirectView
from django.contrib.auth import views

from rest_framework import routers
from apps.api.viewsets import UserViewSet, GroupViewSet, TipoIncidenteViewSet, IncidenteViewSet, \
    AsignacionIncidenteViewSet, CentroEmergenciaViewSet, TipoVehiculoViewSet, VehiculoViewSet, DispositivoGPSViewSet

admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register('usuarios', UserViewSet)
router.register('grupos', GroupViewSet)

router.register('centro-emergencias', CentroEmergenciaViewSet)
router.register('tipo-centro-emergencias', CentroEmergenciaViewSet)
router.register('vehiculos', VehiculoViewSet)
router.register('tipo-vehiculos', TipoVehiculoViewSet)
router.register('dispositivos-gps', DispositivoGPSViewSet)

router.register('incidentes', IncidenteViewSet)
router.register('tipo-incidentes', TipoIncidenteViewSet)
router.register('asignacion-incidentes', AsignacionIncidenteViewSet)

urlpatterns = [

                  path('api/', include(router.urls)),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

                  path('', RedirectView.as_view(url=reverse_lazy('logistica:incidente')), name='index'),
                  path('admin/', admin.site.urls),
                  path('servicios/', include('apps.servicios.urls')),
                  path('administracion/', include('apps.administracion.urls')),
                  path('logistica/', include('apps.logistica.urls')),
                  path('gps/', include('apps.gps.urls')),
                  path('backups/', include('apps.backups.urls')),

                  path('accounts/login/', views.LoginView.as_view(template_name='base/login.html'), name='login'),
                  path('logout', views.LogoutView.as_view(), name='logout'),

                  path('password_reset/',
                       views.PasswordResetView.as_view(template_name='registro/password_reset_form.html',
                                                       email_template_name='registro/password_reset_email.html', ),
                       name='password_reset'),
                  path('password_reset/done/', views.PasswordResetDoneView.as_view(
                      template_name='registro/password_reset_done.html', ), name='password_reset_done'),
                  path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(
                      template_name='registro/password_reset_confirm.html', ), name='password_reset_confirm'),
                  path('reset/done/', views.PasswordResetCompleteView.as_view(
                      template_name='registro/password_reset_complete.html', ), name='password_reset_complete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
