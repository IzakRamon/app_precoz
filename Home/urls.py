from django.urls import path
from Home import views 
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
]