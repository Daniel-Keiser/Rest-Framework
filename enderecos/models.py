from django.db import models


class Endereco(models.Model):
    descricao = models.CharField(max_length=150)
    complemento = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=60)
    pais = models.CharField(max_length=60)

    def __str__(self):
        return self.descricao
    