from django.shortcuts import render
from django.http import JsonResponse
from .models import Pontos
from django.http import request
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.core import serializers
import json
from django.http import HttpResponse

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
    
class SearchResultsView(ListView):
    model = Pontos
    template_name = 'home/exemplo.html'

    def get_queryset(request): # new
        query = request.request.GET.get("q")
        object_list = Pontos.objects.filter(
            Q(Nome__icontains=query)
        )
        
        return object_list
        return render(request, 'home/mainpage.html', object_list)

        qs = serializers.serialize('json', object_list, fields=('latitude', 'longitude', 'Nome', 'preco')[:100])
        qs = json.loads(qs)
        
        print(qs)
        print(object_list)
        
        
        return HttpResponse(json.dumps({"Nome":qs}), content_type='application/json')
        
    
        

        
        



       # return render(request, 'home/exemplo.html', context)
        #return {"IsActive":IsActive}
        #return JsonResponse({'object_list':qs})
        #print(object_list)
        #

    