from django.urls import path

from ..views import mascota_views

urlpatterns = [
    path("", mascota_views.mascota_list, name="mascota_list"),
    path("<int:pk>/", mascota_views.mascota_detail, name="mascota_detail"),
]
