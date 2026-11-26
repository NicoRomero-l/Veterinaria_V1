from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from ..forms.servicio_form import ServicioForm
from ..models import Servicio

def servicio_list(request):
    registros = Paginator(Servicio.objects.select_related("categoria"), 10).get_page(request.GET.get("page"))
    return render(request, "veterinaria_servicios/servicios/lista.html", {"registros": registros})


def servicio_detail(request, pk):
    registro = get_object_or_404(Servicio, pk=pk)
    return render(request, "veterinaria_servicios/servicios/detalle.html", {"registro": registro})

@login_required
@permission_required("veterinaria_servicios.add_servicio", raise_exception=True)
def servicio_create(request):
    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Servicio creado.")
            return redirect("servicio_list")
    else:
        form = ServicioForm()

    return render(request, "veterinaria_servicios/servicios/formulario.html", {
        "form": form,
        "titulo": "Nuevo servicio",
        "ruta_lista": "servicio_list",
    })