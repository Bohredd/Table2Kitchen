from django.db import models

class Mesa(models.Model):
    numero = models.IntegerField()
    nome_cliente = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Mesa {self.numero}"