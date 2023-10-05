from django.shortcuts import render

# Create your views here.
def homePruebas(request):
    return render(request,"homePage/homePruebas.html")