from django.db import models


class Dashboard(models.Model):
    entrada_total = models.FloatField(null=True, blank=True)
    saida_total = models.FloatField(null=True, blank=True)
    saldo = models.FloatField()
    periodo = models.CharField(max_length=50)

