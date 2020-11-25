from django.db import models
from PIL import Image, ImageFilter
from lung.models import Lung
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

class Brain(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=True)
    lung = models.ManyToManyField(Lung)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    enderecos = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True)
    foto = models.ImageField(upload_to = 'brain', null=True, blank=True)
    
def __str__(self):
    return self.nome

    