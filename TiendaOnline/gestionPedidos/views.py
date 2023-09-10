from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
# Create your views here.

class Articulo(object):
        def __init__(self, nombreArticulo,precio):
            self.nombreArticulo=nombreArticulo
            self.precio = precio

def prueba1(request): 
    # vista de prueba
    # Para cargar plantilla
    # fuera del directorio de templates
    # se usa el render de class django.templatebackend.Djando.Template
    print("saludo(request)")
    nombreUsuario="Alejo"
    apellidoUsuario="Dlg"
    Articulo1=Articulo('Sierra',5000)    
    categorias=['Maquinaria','insumos','tecnologia','software']
    fecha_actual=datetime.datetime.now()
    docExterno=open('../TiendaOnline/gestionPedidos/templates/prueba.html')#abro documento
    plt =Template(docExterno.read())#leo documento y lo convierto en un objeto template
    docExterno.close() #cierro comunicacion para ahorrar recursos
    ctx=Context({'nombreUsuario':nombreUsuario,
                 'apellidoUsuario':apellidoUsuario,
                 'fecha_actual':fecha_actual,
                 'nombreArticulo':Articulo1.nombreArticulo,
                 'precio':Articulo1.precio,
                 'categorias':categorias,
                 }) #creo objeto contexto
    
    documento=plt.render(ctx)
    return HttpResponse(documento)

def prueba2(request): 
    # prueba Templates
    # loader carga templates configurados en el [DIR] 
    # se usa el render de class django.template.base.Template
    print("saludo(request)")
    nombreUsuario="Alejo"
    apellidoUsuario="Dlg"
    Articulo1=Articulo('Sierra',5000)    
    categorias=['Maquinaria','insumos','tecnologia','software']
    fecha_actual=datetime.datetime.now()
    docExterno=loader.get_template('template.html')
    ctx={'nombreUsuario':nombreUsuario,
                 'apellidoUsuario':apellidoUsuario,
                 'fecha_actual':fecha_actual,
                 'nombreArticulo':Articulo1.nombreArticulo,
                 'precio':Articulo1.precio,
                 'categorias':categorias,
                 } #creo objeto contexto
    documento=docExterno.render(ctx)
    return HttpResponse(documento)

def prueba3(request): 
    # prueba Templates
    # loader carga templates configurados en el [DIR] 
    # usando el metodo render() ded la libreria shorcuts de django
    print("saludo(request)")
    nombreUsuario="Alejo"
    apellidoUsuario="Dlg"
    Articulo1=Articulo('Sierra',5000)    
    categorias=['Maquinaria','insumos','tecnologia','software']
    fecha_actual=datetime.datetime.now()
    ctx={'nombreUsuario':nombreUsuario,
                 'apellidoUsuario':apellidoUsuario,
                 'fecha_actual':fecha_actual,
                 'nombreArticulo':Articulo1.nombreArticulo,
                 'precio':Articulo1.precio,
                 'categorias':categorias,
                 } #creo objeto contexto
    
    return render(request,'template.html',ctx)


def detalleProducto(request):
    print("detalleProducto(request)")
    fecha={"fecha_actual":datetime.datetime.now()}
    return render(request,'centro\detalleProducto.html',fecha)

def swipeProductos(request):
    print("detalleProducto(request)")
    fecha={"fecha_actual":datetime.datetime.now()}
    return render(request,'centro\swipeProductos.html',fecha)


def despedida(request): # segunda vista 
    print("despedida(request)")
    return HttpResponse("Hasta la vista Baby")

def dameFecha(request): # tercera vista 
    print("dameFecha(request)")
    fecha_actual=datetime.datetime.now()
    documento="""
        <html>
        <head><title></title></head>
        <body style='background-color:yellow;'>
        <h1>la fecha y hora es </h1>
        <p id=fecha>%s</p>
        </html>
        """ % fecha_actual
    return HttpResponse(documento)

def calculaEdad(request,edad,agno): # cuarta vista 
    print("calculaEdad(request)")
    
    periodo=agno-2023
    edadFutura=edad+periodo
    documento="""
        <html>
        <head><title></title></head>
        <body style='background-color:blue;'>
        <h2>En el año %s </h2>
        <p id=edad>tendras %s años</p>
        <p id=edad>Actualmente tienes  %s años</p>
        </html>
        """ %(agno,edadFutura,edad)
    return HttpResponse(documento)