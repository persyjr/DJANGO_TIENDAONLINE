from django.shortcuts import render
from servicios.models import Servicio #modelo servicio de la aplicacion servicios

# Create your views here.
def serviciosVR(request):
    servicios=Servicio.objects.all()
    print(servicios)
    
    return render(request,'servicios/services.html',{"servicios":servicios})