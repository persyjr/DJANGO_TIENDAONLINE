from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos
# Register your models here.

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre','direccion','email','tel')#visualiza los parametross en el admin
    search_fields=('nombre','direccion','email','tel')#barra de busqueda en el admin
    list_filter=('nombre','direccion','email','tel')

@admin.register(Articulos)
class ArticulosAdmin(admin.ModelAdmin):
    list_display=('nombre','seccion','precio')
    search_fields=('nombre','seccion','precio')
    list_filter=('nombre','seccion','precio')

@admin.register(Pedidos)
class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero','fecha','entregado')
    search_fields=('numero','fecha','entregado')
    list_filter=('numero','fecha','entregado')
    date_hierarchy=('fecha')
    
#admin.site.register(Clientes,ClientesAdmin)
#admin.site.register(Articulos,ArticulosAdmin)
#admin.site.register(Pedidos,PedidosAdmin)