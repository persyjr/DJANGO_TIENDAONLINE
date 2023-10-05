from django.shortcuts import render

# Create your views here.
def homeTaller(request):
    return render(request,"homePage/homeTaller.html")