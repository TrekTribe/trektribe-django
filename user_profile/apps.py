from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user_profile"
    verbose_name = "Profilo Utente"

    def ready(self):
        from . import signals  # noqa
