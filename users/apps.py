from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # connecting signals.py to the models in users app.
    def ready(self):
        import users.signals
