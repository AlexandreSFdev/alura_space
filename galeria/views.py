# galeria/views.py

from django.shortcuts import render

def index(request):
    # Renderiza o template index.html (você já consegue acessá-lo)
    return render(request, 'galeria/index.html') 

def imagem(request):
    # Renderiza o template imagem.html
    return render(request, 'galeria/imagem.html')