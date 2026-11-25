from django.contrib import admin

from .models import Categoria, Cita, Mascota, Servicio


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_filter = ("nombre",)
    search_fields = ("nombre", "descripcion")


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especie", "propietario")
    list_filter = ("especie",)
    search_fields = ("nombre", "propietario")


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio")
    list_filter = ("categoria",)
    search_fields = ("nombre", "categoria__nombre")


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ("mascota", "fecha", "creado_por")
    list_filter = ("fecha", "servicios")
    search_fields = ("mascota__nombre", "creado_por__username")
    filter_horizontal = ("servicios",)
