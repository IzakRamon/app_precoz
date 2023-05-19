from django.urls import path
from Home import views 
from . import views

urlpatterns = [
    path("", views.home, name="Home"),

    path('pontos/', views.point, name='listar_pontos')
]