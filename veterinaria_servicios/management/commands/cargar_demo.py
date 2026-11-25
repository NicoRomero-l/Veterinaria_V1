from datetime import date
from decimal import Decimal

from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand
from django.db import transaction

from ...models import Categoria, Cita, Mascota, Servicio


class Command(BaseCommand):
    help = "Carga registros y cuentas de demostración para uso local."

    @transaction.atomic
    def handle(self, *args, **options):
        cuentas = {}
        for nombre, grupo, clave in (
            ("superdemo", None, "VetSuper2026!"),
            ("administrador_demo", "administradores", "VetAdmin2026!"),
            ("consultor_demo", "consultores", "VetConsulta2026!"),
            ("administrador_aux", "administradores", "VetAux2026!"),
        ):
            usuario, creado = User.objects.get_or_create(
                username=nombre,
                defaults={"email": f"{nombre}@example.test", "is_superuser": grupo is None, "is_staff": grupo is None},
            )
            if creado:
                usuario.set_password(clave)
                usuario.save(update_fields=["password"])
                if grupo:
                    usuario.groups.add(Group.objects.get(name=grupo))
            cuentas[nombre] = usuario

        filas = (
            ("Consultas", "Consulta general", "25.00", "Luna", "gato", "Ana Ruiz"),
            ("Vacunación", "Vacuna anual", "30.00", "Toby", "perro", "Luis Paz"),
            ("Higiene", "Baño", "15.00", "Milo", "perro", "Inés León"),
            ("Odontología", "Limpieza dental", "40.00", "Nina", "gato", "Pablo Sol"),
            ("Laboratorio", "Análisis básico", "35.00", "Coco", "otra", "Marta Rey"),
        )
        for numero, (nombre_categoria, nombre_servicio, precio, nombre_mascota, especie, propietario) in enumerate(filas, start=1):
            categoria, _ = Categoria.objects.get_or_create(nombre=nombre_categoria)
            servicio, _ = Servicio.objects.get_or_create(
                nombre=nombre_servicio,
                defaults={"categoria": categoria, "precio": Decimal(precio)},
            )
            mascota, _ = Mascota.objects.get_or_create(
                nombre=nombre_mascota, especie=especie, propietario=propietario
            )
            cita, creada = Cita.objects.get_or_create(
                mascota=mascota,
                fecha=date(2027, 1, numero + 10),
                creado_por=cuentas["administrador_demo"],
            )
            if creada:
                cita.servicios.add(servicio)

        self.stdout.write(self.style.SUCCESS("Datos de demostración cargados."))
