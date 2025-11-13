from django.contrib import admin
from django.urls import include, path   # <-- Certifique-se de que 'include' está importado!

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.galeria.urls')), 
    path('', include('apps.usuarios.urls')),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Comentado para usar S3

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
