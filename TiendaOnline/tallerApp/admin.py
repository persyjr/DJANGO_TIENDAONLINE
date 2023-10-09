from django.contrib import admin
from .models import TallerUser
# Register your models here.
@admin.register(TallerUser)
class PedidosAdmin(admin.ModelAdmin):
    list_display=('nombre','direccion','imagen','email','updated')
    search_fields=('nombre','direccion','email','updated')
    list_filter=('nombre','direccion','email','updated')
    