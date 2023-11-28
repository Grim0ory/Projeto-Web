from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username