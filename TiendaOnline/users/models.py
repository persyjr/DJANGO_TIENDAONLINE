from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.
class User(models.Model):
    nombre=models.CharField(max_length=30, unique=True)
    direccion=models.CharField(max_length=50,verbose_name='Domicilio Cliente',blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    tel=models.CharField(max_length=7,blank=True,null=True)
    imagen=models.ImageField(upload_to='servicios',blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    historical=HistoricalRecords()

    def __str__(self):
        return "Usuario nombre: %s"%(self.nombre)
    
    class Meta:
        verbose_name='Usuaio'
        verbose_name_plural='Usuarios'