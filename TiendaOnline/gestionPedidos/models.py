from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50,verbose_name='Domicilio Cliente')
    email=models.EmailField(blank=True,null=True)
    tel=models.CharField(max_length=7)
    def __str__(self):
        return "Cliente nombre: %s"%(self.nombre)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return "Articulo nombre: %s seccion: %s "%(self.nombre,self.seccion)
    
class Pedidos(models.Model):
    numero=models.CharField(max_length=30)
    fecha=models.DateField()
    entregado=models.BooleanField()
    def __str__(self):
        return "Pedido numero: %s entregado: %s "%(self.numero,self.entregado)