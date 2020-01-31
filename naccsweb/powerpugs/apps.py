from django.apps import AppConfig
from django.conf import settings as django_settings

class PPConfig(AppConfig):
    name = 'powerpugs'
    def ready(self):
        return