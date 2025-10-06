from django.shortcuts import render

from galeria.models import Fotografia

# Create your views here.

def index(request):
    fotografias = Fotografia.objects.all()
    # Renderiza o template index.html (você já consegue acessá-lo)
    return render(request, 'galeria/index.html', {"cards": fotografias}) 

def imagem(request):
    # Renderiza o template imagem.html
    return render(request, 'galeria/imagem.html')