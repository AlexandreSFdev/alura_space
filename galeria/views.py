from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia

# Create your views here.

def index(request):
    fotografias = Fotografia.objects.all()
    # Renderiza o template index.html (você já consegue acessá-lo)
    return render(request, 'galeria/index.html', {"cards": fotografias}) 

def imagem(request, foto_id):
    # Renderiza o template imagem.html
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})