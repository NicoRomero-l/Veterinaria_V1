from django.urls import path

from ..views import categoria_views

urlpatterns = [
    path("", categoria_views.categoria_list, name="categoria_list"),
    path("<int:pk>/", categoria_views.categoria_detail, name="categoria_detail"),
    path("crear/", categoria_views.categoria_create, name="categoria_create"),
    path("<int:pk>/editar/", categoria_views.categoria_update, name="categoria_update"),
    path("<int:pk>/eliminar/", categoria_views.categoria_delete, name="categoria_delete"),
]
