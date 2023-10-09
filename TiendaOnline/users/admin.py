from django.contrib import admin
from users.models import User
# Register your models here.

@admin.register(User)
class PedidosAdmin(admin.ModelAdmin):
    list_display=('nombre','direccion','email','tel','imagen','created','updated','historical')
    
    list_filter=('nombre','direccion','email','tel','created','updated')