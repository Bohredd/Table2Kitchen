from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()
    descricao = models.TextField()
    categorias = models.ManyToManyField(Categoria, related_name="produtos")
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to="produtos", null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome