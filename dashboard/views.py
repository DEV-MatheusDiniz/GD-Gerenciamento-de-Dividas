from django.shortcuts import render

from .models import Dashboard
from entrada.models import Entrada
from saida.models import Saida




def func_dashboard(periodo):
    entrada_total: float = 0
    saida_total: float = 0

    entradas = Entrada.objects.filter(periodo=periodo)
    saidas = Saida.objects.filter(periodo=periodo)
    
    for entrada in entradas:
        entrada_total += entrada.valor
            
    for saida in saidas:
        saida_total += saida.valor_parcela

    Dashboard.objects.filter(periodo=periodo).delete()

    Dashboard(
        entrada_total = entrada_total,
        saida_total = saida_total,
        saldo = entrada_total - saida_total,
        periodo = periodo
    ).save()

    return None
    
