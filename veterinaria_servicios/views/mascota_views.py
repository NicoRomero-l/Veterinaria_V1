from django.shortcuts import get_object_or_404, render

from ..models import Mascota


def mascota_list(request):
    return render(request, "veterinaria_servicios/mascotas/lista.html", {"registros": Mascota.objects.all()})


def mascota_detail(request, pk):
    registro = get_object_or_404(Mascota, pk=pk)
    return render(request, "veterinaria_servicios/mascotas/detalle.html", {"registro": registro})
