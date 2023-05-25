from django.urls import path
from django.urls import path, include
from Home import views 
from . import views
from . import *

urlpatterns = [
    path("", views.home, name="Home"),
    path('json/', views.jsondata),
    path('pontos/', views.point, name='listar_pontos')
    
]