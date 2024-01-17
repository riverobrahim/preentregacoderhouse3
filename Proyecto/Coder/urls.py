

from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("venderdor/list", views.vendedor_list, name="vendedor_list"),
    path("venderdor/form", views.vendedor_form, name="vendedor_form"),
    
    ]
