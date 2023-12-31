from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.

class TallerUser(models.Model):
    nombre=models.CharField(max_length=30, unique=True)
    direccion=models.CharField(max_length=50,verbose_name='Domicilio Taller',blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    tel=models.CharField(max_length=7,blank=True,null=True)
    imagen=models.ImageField(upload_to='tallerUsers',blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    historical=HistoricalRecords()

    def __str__(self):
        return "Taller nombre: %s"%(self.nombre)
    
    class Meta:
        verbose_name='Taller'
        verbose_name_plural='Talleres'

