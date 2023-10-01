from django.urls import path
from gestionPedidos.views import prueba1, prueba2, prueba3, despedida, dameFecha, calculaEdad,detalleProducto,swipeProductos,contacto

urlpatterns = [
    #URLS gestionPedidos
    path('prueba1/', prueba1),
    path('prueba2/', prueba2),
    path('prueba3/', prueba3),
    path('detalleProducto/', detalleProducto),
    path('swipeProductos/', swipeProductos),
    path('despedida/', despedida),
    path('contacto/', contacto),
    path('fecha/', dameFecha),
    path('edad/<int:edad>/<int:agno>/', calculaEdad),#aca importo un dato con el cual hago un calculo en mi funcion edad
]