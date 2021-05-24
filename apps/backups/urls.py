from django.conf.urls import url
from django.urls import path
from .views import BackupView

app_name = 'backups'

urlpatterns = [
    path('download/', BackupView.as_view(), name="backups_view"),
]
