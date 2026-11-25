from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models.deletion import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from ..forms import CategoriaForm
from ..models import Categoria


def categoria_list(request):
    return render(request, "veterinaria_servicios/categorias/lista.html", {"registros": Categoria.objects.all()})


def categoria_detail(request, pk):
    registro = get_object_or_404(Categoria, pk=pk)
    return render(request, "veterinaria_servicios/categorias/detalle.html", {"registro": registro})


@login_required
@permission_required("veterinaria_servicios.add_categoria", raise_exception=True)
def categoria_create(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro creado.")
            return redirect("categoria_list")
    else:
        form = CategoriaForm()
    return render(request, "veterinaria_servicios/categorias/formulario.html", {"form": form, "titulo": "Crear categoria"})


@login_required
@permission_required("veterinaria_servicios.change_categoria", raise_exception=True)
def categoria_update(request, pk):
    registro = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            messages.success(request, "Cambios guardados.")
            return redirect(registro)
    else:
        form = CategoriaForm(instance=registro)
    return render(request, "veterinaria_servicios/categorias/formulario.html", {"form": form, "titulo": "Editar categoria"})


@login_required
@permission_required("veterinaria_servicios.delete_categoria", raise_exception=True)
def categoria_delete(request, pk):
    registro = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        try:
            registro.delete()
        except ProtectedError:
            messages.error(request, "La categoría tiene servicios asociados.")
            return redirect(registro)
        messages.success(request, "Registro eliminado.")
        return redirect("categoria_list")
    return render(request, "veterinaria_servicios/categorias/confirmar_eliminacion.html", {"registro": registro})
