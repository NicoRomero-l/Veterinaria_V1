from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from ..models import Mascota


def mascota_list(request):
    registros = Paginator(Mascota.objects.all(), 10).get_page(request.GET.get("page"))
    return render(request, "veterinaria_servicios/mascotas/lista.html", {"registros": registros})


def mascota_detail(request, pk):
    registro = get_object_or_404(Mascota, pk=pk)
    return render(request, "veterinaria_servicios/mascotas/detalle.html", {"registro": registro})
