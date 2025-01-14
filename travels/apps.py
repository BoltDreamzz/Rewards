

from django.apps import AppConfig

class TravelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'travels'

    def ready(self):
        import travels.signals  # Import the signals module to register the signal