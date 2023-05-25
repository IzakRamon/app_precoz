from django.shortcuts import render
from django.http import JsonResponse
from .models import Pontos
from django.http import request

def home(request):
    return render(request, 'home/exemplo.html', {})

def point(request):
    
    novo_ponto = Pontos()
    novo_ponto.Nome = request.POST.get('Nome')
    novo_ponto.preco = request.POST.get('preco')
    novo_ponto.latitude = request.POST.get('lat')
    novo_ponto.longitude = request.POST.get('lon')
    novo_ponto.save()

    point = {'point': Pontos.objects.all()}
    return render(request, 'home/exemplo.html', point)

def jsondata(request):
    data = list(Pontos.objects.values('latitude', 'longitude', 'Nome', 'preco')[:100])
    print(data[:2])
    context = {'data': data}
    return render(request, 'home/exemplo.html', context)
    
