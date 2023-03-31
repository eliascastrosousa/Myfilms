from django.db import models

class Lista(models.Model):
    nome = models.CharField(max_length=100)
    tipo_filme = models.CharField(max_length=100)
    concluido = models.BooleanField(default=False)
    resenha = models.TextField()

    def __str__(self):
        return self.nome


