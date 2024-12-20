from django.db import models

class Garcom(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    restaurante = models.ForeignKey('cozinha.Restaurante', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome