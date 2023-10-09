from django.contrib import admin
from .models import Servicio ,TallerTask
# Register your models here.


@admin.register(Servicio)
class PedidosAdmin(admin.ModelAdmin):
    list_display=('titulo','contenido','imagen','created','updated')
    search_fields=('titulo','contenido','imagen','created','updated')
    list_filter=('titulo','contenido','imagen','created','updated')
    
@admin.register(TallerTask)
class PedidosAdmin(admin.ModelAdmin):
    list_display=('creada_por','asignada_a','departamentos_asociados','entregado','creacion_tarea')
    search_fields=('creada_por','asignada_a','departamentos_asociados','entregado','creacion_tarea')
    list_filter=('creada_por','asignada_a','departamentos_asociados','entregado','creacion_tarea')
    