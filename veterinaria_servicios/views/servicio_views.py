from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from ..models import Servicio


def servicio_list(request):
    registros = Paginator(Servicio.objects.select_related("categoria"), 10).get_page(request.GET.get("page"))
    return render(request, "veterinaria_servicios/servicios/lista.html", {"registros": registros})


def servicio_detail(request, pk):
    registro = get_object_or_404(Servicio, pk=pk)
    return render(request, "veterinaria_servicios/servicios/detalle.html", {"registro": registro})
