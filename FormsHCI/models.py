from django.db import models
import csv


class Domanda(models.Model):

    testoDomanda = models.CharField(max_length=200)

    def __str__(self):
        return Domanda.testoDomanda


class RispostaSUS(models.Model):

    OPTIONS = (('1', '1'),
               ('2', '2'),
               ('3', '3'),
               ('4', '4'),
               ('5', '5'))

    domanda = models.ForeignKey(Domanda, on_delete=models.CASCADE)
    scelta = models.IntegerField(choices=OPTIONS, default=0)

    def __str__(self):
        return self.domanda, self.scelta


class SUSModel(models.Model):

    nome = models.CharField("Nome", max_length=400)

    def __str__(self):
        return self.nome

# risposta multipla del sus
# class Risposta(models.Model):
