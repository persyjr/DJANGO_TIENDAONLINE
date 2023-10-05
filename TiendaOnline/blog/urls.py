from django.urls import path
from .views import  blogVR
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    #URLS villaRaquel
    path('blogVR/', blogVR),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)