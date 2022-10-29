from django.shortcuts import redirect, render

from .models import Entrada
from saida.models import Saida
from dashboard.models import Dashboard

from dashboard.views import func_dashboard

from datetime import date


# MOTRA ENTRADA E SAIDAS DO MES
def home(request):
    # CAPTURAR DATA ATUAL
    periodo = str(date.today())[:7]
    # SELECT COM DATA ATUAL
    entradas = Entrada.objects.filter(periodo=periodo)
    saidas = Saida.objects.filter(periodo=periodo)
    dashboard = Dashboard.objects.filter(periodo=periodo)


    if request.method == 'POST':
        # CAPTURAR DATA E PAGO
        periodo = request.POST.get('periodo')
        id = request.POST.get('id')
        pago = bool(request.POST.get('pago'))

        if periodo:
            # SELECT
            entradas = Entrada.objects.filter(periodo=periodo)
            saidas = Saida.objects.filter(periodo=periodo)
            dashboard = Dashboard.objects.filter(periodo=periodo)
        else:
            Saida.objects.filter(
                id=id
            ).update(
                pago=pago
            )
            
    return render(request, 'entrada_saida.html', {'mostra_filtro':True, 'entradas':entradas, 'saidas':saidas, 'periodo':periodo, 'dashboard': dashboard})


# ADICIONAR NOVA ENTRADA
def adicionar_entrada(request):
    if request.method == 'POST':
        # CAPTURAR DADOS
        titulo = request.POST['titulo']
        valor = float(request.POST['valor'])
        periodo = request.POST['periodo']
        # SALVAR ENTRADA
        Entrada(
            titulo = titulo, 
            valor = valor, 
            periodo = periodo,
        ).save()
        # SALVAR DASHBOARD
        func_dashboard(periodo = periodo)

        return redirect('mostra_entrada_saida')
    return render(request, 'entrada/form_entrada.html')


# ALTERAR ENTRADA
def alterar_entrada(request, id):
    # SELECT
    entrada = Entrada.objects.get(id=id)

    if request.method == 'POST':
        # CAPTURAR DADOS
        titulo = request.POST['titulo']
        valor = float(request.POST['valor'])
        periodo = request.POST['periodo']
        # SALVAR ENTRADA
        entrada = Entrada(
            id=id,
            titulo = titulo, 
            valor = valor,
            periodo = periodo
        ).save()
        # SALVAR DASHBOARD
        func_dashboard(periodo=periodo)

        return redirect('mostra_entrada_saida')
    return render(request, 'entrada/form_entrada.html', {'entrada':entrada})


# REMOVER ENTRADA
def remover_entrada(request, id):
    # SELECT
    entrada = Entrada.objects.get(id=id)

    if request.method == 'POST':
        # DELETAR DADO
        entrada.delete()
        # ATUALIZAR DASHBOAR
        func_dashboard(periodo = entrada.periodo)
        return redirect('mostra_entrada_saida')
    return render(request, 'confirma_remover.html', {'entrada': entrada})

