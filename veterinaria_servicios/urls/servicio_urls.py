from django.urls import path

from ..views import servicio_views

urlpatterns = [
    path("", servicio_views.servicio_list, name="servicio_list"),
    path("<int:pk>/", servicio_views.servicio_detail, name="servicio_detail"),
]
