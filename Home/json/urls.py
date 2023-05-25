from django.urls import path
from Home import views 
from json import urls
from . import *

urlpatterns = [
    path('',views.jsondata,name = "jsondata")
]