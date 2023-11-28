from django.db import models


class Barbeiro(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    username = models.CharField(max_length=60)
    
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Servico(models.Model):
    titulo = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.titulo

