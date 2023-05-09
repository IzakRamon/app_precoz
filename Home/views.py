from django.shortcuts import render
from .models import Pontos
 

def home(request):
    return render(request, 'home/exemplo.html', {})

