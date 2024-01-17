from django import forms

from . import models

class Vendedorform(forms.ModelForm):
    class Meta:
        model = models.vendedor
        fields = "__all__"