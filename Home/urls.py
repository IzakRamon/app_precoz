from django.urls import path
from django.urls import path, include
from Home import views 
from . import views
from . import *
from .views import SearchResultsView

urlpatterns = [
    path("", views.home, name="Home"),
    path('json/', views.jsondata, name="buscar_preco"),
    path('pontos/', views.point, name='listar_pontos'),
    path('search/', SearchResultsView.as_view(), name='search_preco'),
    
]