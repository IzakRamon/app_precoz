from django.conf import settings
from django.db import models
from django.utils import timezone


class Pontos(models.Model):
    id_ponto = models.IntegerField(primary_key=True, default= 000)
    nome_ponto = models.CharField(max_length= 250)
    preco = models.IntegerField(default= 0)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.nome_ponto
    