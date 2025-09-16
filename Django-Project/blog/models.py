from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome
    








