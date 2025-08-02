from django.apps import AppConfig

class ReviewpostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviewpost'

    def ready(self):
        import reviewpost.models