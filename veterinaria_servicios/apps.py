from django.apps import AppConfig
from django.db.models.signals import post_migrate


class VeterinariaServiciosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "veterinaria_servicios"

    def ready(self):
        from .permisos import configurar_grupos

        post_migrate.connect(configurar_grupos, sender=self)
