from django.urls import path

from ..views import cerrar_sesion, iniciar_sesion, registro

urlpatterns = [
    path("registro/", registro, name="registro"),
    path("login/", iniciar_sesion, name="login"),
    path("logout/", cerrar_sesion, name="logout"),
]
