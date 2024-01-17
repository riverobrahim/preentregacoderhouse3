from django.db import models

class vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre
    
class Compra(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()
    vendedor = models.ForeignKey(vendedor, on_delete= models.SET_NULL, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.nombre}-{self.vendedor}"
    
    
class ClientePorCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.compra}-{self.cliente}"
    