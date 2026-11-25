from django.urls import path

from ..views import cita_views

urlpatterns = [
    path("", cita_views.cita_list, name="cita_list"),
    path("<int:pk>/", cita_views.cita_detail, name="cita_detail"),
    path("crear/", cita_views.cita_create, name="cita_create"),
    path("<int:pk>/editar/", cita_views.cita_update, name="cita_update"),
    path("<int:pk>/eliminar/", cita_views.cita_delete, name="cita_delete"),
]
