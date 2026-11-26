from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from ..forms.mascota_form import MascotaForm
from ..models import Mascota


def mascota_list(request):
    registros = Paginator(Mascota.objects.all(), 10).get_page(request.GET.get("page"))
    return render(request, "veterinaria_servicios/mascotas/lista.html", {"registros": registros})


def mascota_detail(request, pk):
    registro = get_object_or_404(Mascota, pk=pk)
    return render(request, "veterinaria_servicios/mascotas/detalle.html", {"registro": registro})

@login_required
@permission_required("veterinaria_servicios.add_mascota", raise_exception=True)
def mascota_create(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mascota creada.")
            return redirect("mascota_list")
    else:
        form = MascotaForm()

    return render(request, "veterinaria_servicios/mascotas/formulario.html", {
        "form": form,
        "titulo": "Nueva mascota",
        "ruta_lista": "mascota_list",
    })