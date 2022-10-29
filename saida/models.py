from django.db import models


# SAIDA
class Saida(models.Model):
    titulo = models.CharField(max_length=100)
    periodo = models.CharField(max_length=50)
    parcela = models.IntegerField()
    qtd_parcela = models.IntegerField()
    valor_parcela = models.FloatField()
    pago = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.titulo
        