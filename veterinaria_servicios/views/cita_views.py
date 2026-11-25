from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from ..forms import CitaForm
from ..models import Cita


@login_required
@permission_required("veterinaria_servicios.view_cita", raise_exception=True)
def cita_list(request):
    registros = Paginator(Cita.objects.select_related("mascota"), 10).get_page(request.GET.get("page"))
    return render(request, "veterinaria_servicios/citas/lista.html", {"registros": registros})


@login_required
@permission_required("veterinaria_servicios.view_cita", raise_exception=True)
def cita_detail(request, pk):
    registro = get_object_or_404(Cita, pk=pk)
    return render(request, "veterinaria_servicios/citas/detalle.html", {"registro": registro})


@login_required
@permission_required("veterinaria_servicios.add_cita", raise_exception=True)
def cita_create(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                cita = form.save(commit=False)
                cita.creado_por = request.user
                cita.save()
                form.save_m2m()
            messages.success(request, "Registro creado.")
            return redirect("cita_list")
    else:
        form = CitaForm()
    return render(request, "veterinaria_servicios/citas/formulario.html", {"form": form, "titulo": "Crear cita"})


@login_required
@permission_required("veterinaria_servicios.change_cita", raise_exception=True)
def cita_update(request, pk):
    registro = get_object_or_404(Cita, pk=pk)
    if registro.creado_por_id != request.user.pk and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == "POST":
        form = CitaForm(request.POST, instance=registro)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            messages.success(request, "Cambios guardados.")
            return redirect(registro)
    else:
        form = CitaForm(instance=registro)
    return render(request, "veterinaria_servicios/citas/formulario.html", {"form": form, "titulo": "Editar cita"})


@login_required
@permission_required("veterinaria_servicios.delete_cita", raise_exception=True)
def cita_delete(request, pk):
    registro = get_object_or_404(Cita, pk=pk)
    if registro.creado_por_id != request.user.pk and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == "POST":
        registro.delete()
        messages.success(request, "Registro eliminado.")
        return redirect("cita_list")
    return render(request, "veterinaria_servicios/citas/confirmar_eliminacion.html", {"registro": registro})
