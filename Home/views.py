from django.shortcuts import render
from .models import Pontos
import folium 

def home(request):
    return render(request, 'home/exemplo.html', {})

