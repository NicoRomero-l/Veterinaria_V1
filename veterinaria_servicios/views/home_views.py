from django.shortcuts import render

from ..models import Categoria, Cita, Mascota, Servicio


def home(request):
    return render(request, "veterinaria_servicios/inicio.html", {
        "total_categorias": Categoria.objects.count(),
        "total_mascotas": Mascota.objects.count(),
        "total_servicios": Servicio.objects.count(),
        "total_citas": Cita.objects.count(),
    })
