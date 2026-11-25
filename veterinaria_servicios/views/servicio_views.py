from django.shortcuts import get_object_or_404, render

from ..models import Servicio


def servicio_list(request):
    return render(request, "veterinaria_servicios/servicios/lista.html", {"registros": Servicio.objects.all()})


def servicio_detail(request, pk):
    registro = get_object_or_404(Servicio, pk=pk)
    return render(request, "veterinaria_servicios/servicios/detalle.html", {"registro": registro})
