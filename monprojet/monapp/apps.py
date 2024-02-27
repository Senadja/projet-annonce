from django.apps import AppConfig


class MonappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monapp'

def ready(self):
    """
    Override this method to perform initialization tasks such as registering signals.
    It is called as soon as the registry is fully populated.
    """
    pass
