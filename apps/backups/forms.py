# encoding:utf-8
from django import forms
from django.conf import settings
from crispy_forms.helper import FormHelper
from .utils import backup_database, backup_media


class DatabaseBackupForm(forms.Form):
    helper = FormHelper()
    helper.form_tag = False

    database = forms.ChoiceField(widget=forms.Select(attrs={'class': 'select form-control'}),
        label='Elija una base de datos para hacer una copia',
        choices=zip(
            settings.DATABASES.keys(),
            settings.DATABASES.keys()
        )
    )

    def do_backup(self):
        return backup_database(self.cleaned_data['database'])


class MediaBackupForm(forms.Form):

    def do_backup(self):
        return backup_media()