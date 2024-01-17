from django.shortcuts import redirect, render

from . import models
from . import forms

def index(request):
    return render(request, "Coder/index.html")

def vendedor_list(request):
    consulta = models.vendedor.objects.all()
    contexto = {"vendedores": consulta}
    return render(request, "Coder/vendedor_list.html",contexto)

def vendedor_form(request):
    if request.method == "POST":
        form = forms.Vendedorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vendedor_list")
            
    else:
        form = forms.Vendedorform()
    return render(request, "Coder/vendedor_form.html", {"form" : form})

