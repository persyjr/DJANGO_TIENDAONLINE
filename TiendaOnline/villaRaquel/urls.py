from django.urls import path
from villaRaquel.views import contactoVR, homeVR, tiendaVR, blogVR
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    #URLS villaRaquel
    path('contactoVR/', contactoVR),
    path('homeVR/', homeVR),
    path('tiendaVR/',tiendaVR),
    path('blogVR/', blogVR),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)