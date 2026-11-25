from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Group, Permission


def configurar_grupos(sender, using, **kwargs):
    create_permissions(sender, using=using, verbosity=0)
    permisos = Permission.objects.using(using).filter(content_type__app_label=sender.label)
    consultores, _ = Group.objects.using(using).get_or_create(name="consultores")
    administradores, _ = Group.objects.using(using).get_or_create(name="administradores")
    consultores.permissions.set(permisos.filter(codename__startswith="view_"))
    administradores.permissions.set(permisos)
