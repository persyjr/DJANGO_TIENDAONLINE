from django.shortcuts import render

# Create your views here.
def homeVR(request):
    return render(request,'homePage\home.html')

def tiendaVR(request):
    return render(request,'tienda\\tienda.html')
def blogVR(request):
    return render(request,'blog\\blog.html')
def contactoVR(request):
    return render(request,'contact\contact.html')
