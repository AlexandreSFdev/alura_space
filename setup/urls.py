# setup/urls.py

from django.contrib import admin
from django.urls import path, include  # <-- Certifique-se de que 'include' está importado!

urlpatterns = [
    path('admin/', admin.site.urls),
    # Adiciona a rota raiz ('') para incluir as URLs da aplicação 'galeria'
    path('', include('galeria.urls')), 
]
