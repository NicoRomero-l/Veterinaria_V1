from django import forms

from ..models import Cita


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ["mascota", "servicios", "fecha"]
        widgets = {"fecha": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d")}
