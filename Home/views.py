from django.shortcuts import render
from .models import Pontos
from django.http import request

 

def home(request):
    return render(request, 'home/exemplo.html', {})

def point(request):
    
    novo_ponto = Pontos()
    novo_ponto.Nome = request.POST.get('Nome')
    novo_ponto.preco = request.POST.get('preco')
    
    novo_ponto.save()

    point = {
        'point': Pontos.objects.all()
    }

    return render(request, 'home/exemplo.html', point)
