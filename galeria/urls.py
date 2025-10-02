# galeria/urls.py

from django.urls import path
from galeria.views import index, imagem # <-- Você precisará criar essas views

urlpatterns = [
    # Mapeia a URL raiz da galeria para a função 'index'
    path('', index, name='index'), 
    
    # Mapeia a URL 'imagem.html' para a função 'imagem'
    path('imagem/', imagem, name='imagem'), 
]