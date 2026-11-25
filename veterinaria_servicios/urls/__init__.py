from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="categoria_list"), name="inicio"),
    path("categorias/", include("veterinaria_servicios.urls.categoria_urls")),
    path("mascotas/", include("veterinaria_servicios.urls.mascota_urls")),
    path("servicios/", include("veterinaria_servicios.urls.servicio_urls")),
    path("citas/", include("veterinaria_servicios.urls.cita_urls")),
]
