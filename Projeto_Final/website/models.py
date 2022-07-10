from django.db import models

class AFD(models.Model):
    descricao = models.CharField(max_length=200)
    alfabeto = models.CharField(max_length=200)
    estados = models.CharField(max_length=200)
    estadoinicial = models.CharField(max_length=200)
    estadosdeaceitacao = models.CharField(max_length=200)
    tabeladetransicoes = models.CharField(max_length=600)


    def __str__(self):
        return self.descricao[:50]

class TM(models.Model):
    descricao = models.CharField(max_length=200)
    estados = models.CharField(max_length=200)
    estadoinicial = models.CharField(max_length=200)
    estadodeaceitacao = models.CharField(max_length=200)
    tabeladetransicoes = models.CharField(max_length=600)

    def __str__(self):
        return self.descricao[:50]