from django.contrib import admin

from . import models

admin.site.register(models.vendedor)
admin.site.register(models.Cliente)
admin.site.register(models.Compra)
admin.site.register(models.ClientePorCompra)


