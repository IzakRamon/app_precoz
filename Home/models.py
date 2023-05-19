from django.conf import settings
from django.db import models
from django.utils import timezone


class Pontos(models.Model):
    id_ponto = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100, null=True)
    preco = models.IntegerField(default= 0, null=True)
    

  
    