from django.db import models


# ENTRADA
class Entrada(models.Model):
    titulo = models.CharField(max_length=100)
    valor = models.FloatField()
    periodo = models.CharField(max_length=50)
    recebido = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.titulo
