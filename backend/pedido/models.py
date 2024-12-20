from django.db import models

class StatusPedido(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    mesa = models.ForeignKey('mesa.Mesa', on_delete=models.CASCADE)
    garcom = models.ForeignKey('garcom.Garcom', on_delete=models.CASCADE)
    produtos = models.ManyToManyField('produto.Produto')
    
    horario_pedido = models.DateTimeField(auto_now_add=True)

    status = models.ForeignKey(StatusPedido, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido {self.id} - {self.mesa} - {self.garcom}"