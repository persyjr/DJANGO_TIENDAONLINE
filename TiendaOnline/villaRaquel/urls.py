from django.urls import path
from villaRaquel.views import contactoVR, homeVR, serviciosVR, tiendaVR, blogVR

urlpatterns = [    
    #URLS villaRaquel
    path('contactoVR/', contactoVR),
    path('homeVR/', homeVR),
    path('serviciosVR/', serviciosVR),
    path('tiendaVr/',tiendaVR),
    path('blogVR/', blogVR),
]