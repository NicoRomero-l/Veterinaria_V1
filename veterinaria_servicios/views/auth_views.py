from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.db import transaction
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from ..forms import RegistroForm


def registro(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                usuario = form.save()
                usuario.groups.add(Group.objects.get(name="consultores"))
            messages.success(request, "Cuenta creada. Ya puedes iniciar sesión.")
            return redirect("login")
    else:
        form = RegistroForm()
    return render(request, "veterinaria_servicios/auth/registro.html", {"form": form})


def iniciar_sesion(request):
    destino = request.POST.get("next") or request.GET.get("next") or ""
    if not url_has_allowed_host_and_scheme(
        destino, allowed_hosts={request.get_host()}, require_https=request.is_secure()
    ):
        destino = ""

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(destino or settings.LOGIN_REDIRECT_URL)
    else:
        form = AuthenticationForm(request)

    return render(request, "veterinaria_servicios/auth/login.html", {
        "form": form,
        "next": destino,
    })


@require_POST
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
