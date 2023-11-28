from django.db import models
from django.contrib.auth.models import User
from barbearia.models import *

class Agenda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
   