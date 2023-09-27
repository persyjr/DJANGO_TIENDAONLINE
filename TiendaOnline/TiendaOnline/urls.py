"""
URL configuration for TiendaOnline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionPedidos.views import prueba1, prueba2, prueba3, despedida, dameFecha, calculaEdad,detalleProducto,swipeProductos,contacto
urlpatterns = [
    path('admin/', admin.site.urls),
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
