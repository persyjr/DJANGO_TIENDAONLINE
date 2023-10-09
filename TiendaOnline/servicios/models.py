from django.db import models
from users.models import User
from tallerApp.models import TallerUser
# Create your models here.
class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Servicio nombre: %s"%(self.titulo)
    class Meta:
        verbose_name='servicio'
        verbose_name_plural='Servicios'

class TallerTask(models.Model):
    creada_por=models.ForeignKey(User, on_delete=models.CASCADE)# Preguntar si dejar configurado on_Delete para eliminar todo el historial 
    asignada_a=models.ForeignKey(TallerUser, on_delete=models.CASCADE)
    nombre_tarea=models.CharField(max_length=30,null=True)
    departamentos_asociados=models.CharField(max_length=30, null=True)
    creacion_tarea=models.DateTimeField(auto_now_add=True)
    fecha=models.DateField()
    entregado=models.BooleanField()
    def __str__(self):
        return "Name TallerTask: %s creacion: %s "%(self.nombre_tarea,self.creacion_tarea)
    class Meta:
        verbose_name='TallerTask'
        verbose_name_plural='TallerTasks'