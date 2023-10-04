from django.contrib import admin
from .models import Servicio
# Register your models here.


@admin.register(Servicio)
class PedidosAdmin(admin.ModelAdmin):
    list_display=('titulo','contenido','imagen','created','updated')
    search_fields=('titulo','contenido','imagen','created','updated')
    list_filter=('titulo','contenido','imagen','created','updated')
    
