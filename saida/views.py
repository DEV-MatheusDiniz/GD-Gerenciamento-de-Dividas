from django.shortcuts import redirect, render

from .models import Saida
from dashboard.views import func_dashboard

meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']




# ADICIONAR NOVA SAIDA
def adicionar_saida(request):
    if request.method == 'POST':
        # FUNÇÃO DAS PARCELAS
        def func_parcela(titulo, periodo, qtd_parcela, valor_parcela):
                if qtd_parcela > 1:
                    for x in range(qtd_parcela):
                        # salvar dados
                        Saida(
                            titulo = titulo,
                            periodo = periodo,
                            parcela = x+1,
                            qtd_parcela = qtd_parcela,
                            valor_parcela = valor_parcela,
                        ).save()
                        # atualizar dashboard
                        func_dashboard(periodo = periodo)

                        # capturar mes e ano
                        mes = int(periodo[5:])
                        ano = int(periodo[:4])
                        # SOMATORIA
                        if int(mes) == 12:
                            mes = meses[0]
                            ano += 1
                        else:
                            mes = meses[mes]
                        periodo = str(ano) + '-' + str(mes)
                else:
                    # salvar dados
                    Saida(
                        titulo = titulo,
                        periodo = periodo,
                        parcela = qtd_parcela,
                        qtd_parcela = qtd_parcela,
                        valor_parcela = valor_parcela,
                    ).save()
                    # atualizar dashboard
                    func_dashboard(periodo = periodo)


        # capturar dados
        titulo = request.POST['titulo']
        periodo = request.POST['periodo']
        qtd_parcela = int(request.POST['qtd_parcela'])
        valor_parcela = float(request.POST['valor_parcela'])

        # FUNÇÃO DAS PARCELAS
        func_parcela(titulo, periodo, qtd_parcela, valor_parcela)
        
        return redirect('mostra_entrada_saida')
    return render(request, 'saida/form_saida.html')


# ALTERAR SAIDA
def alterar_saida(request, id):
    # SELECT
    saida = Saida.objects.get(id=id)

    if request.method == 'POST':
        def alterar_mes_em_diante(titulo, periodo, parcela, qtd_parcela, valor_parcela):
                repete = abs(saida.parcela - qtd_parcela)
                cont=0
                while cont <= repete:
                    Saida.objects.filter(
                        titulo = saida.titulo,
                        parcela = parcela+cont,
                    ).update(
                        titulo = titulo,
                        periodo = periodo,
                        parcela = parcela+cont,
                        valor_parcela = valor_parcela,
                    )
                    # atualizar dashboard
                    func_dashboard(periodo = periodo)

                    cont += 1
                    # capturar mes e ano
                    mes = int(periodo[5:])
                    ano = int(periodo[:4])
                    # SOMATORIA
                    if int(mes) == 12:
                        mes = meses[0]
                        ano += 1
                    else:
                        mes = meses[mes]
                    periodo = str(ano) + '-' + str(mes)
        def alterar_mes_atual(titulo, periodo, parcela, qtd_parcela, valor_parcela):
            Saida.objects.filter(
                id=id
            ).update(
                titulo = titulo,
                periodo = periodo,
                parcela = parcela,
                qtd_parcela = qtd_parcela,
                valor_parcela = valor_parcela,
            )
            # atualizar dashboard
            func_dashboard(periodo = periodo)

        # capturar dados
        titulo = request.POST['titulo']
        periodo = request.POST['periodo']
        parcela = saida.parcela
        qtd_parcela = saida.qtd_parcela
        valor_parcela = float(request.POST['valor_parcela'])

        verifica = request.POST.get('alterar_mes_em_diante', False)
        if verifica:
            alterar_mes_em_diante(titulo, periodo, parcela, qtd_parcela, valor_parcela)
        else:
            alterar_mes_atual(titulo, periodo, parcela, qtd_parcela, valor_parcela)

        return redirect('mostra_entrada_saida')
    return render(request, 'saida/form_saida.html', {'saida':saida})


# REMOVER SAIDA
def remover_saida(request, id):
    # SELECT
    saida = Saida.objects.get(id=id)

    if request.method == 'POST':
        def remover_mes_em_diante(periodo):
            repete = abs(saida.parcela - saida.qtd_parcela)
            cont=0
            while cont <= repete:
                Saida.objects.filter(
                    titulo = saida.titulo,
                    periodo = periodo,
                    parcela = saida.parcela+cont
                ).delete()
                # atualizar dashboard
                func_dashboard(periodo = periodo)

                cont+=1
                # capturar mes e ano
                mes = int(periodo[5:])
                ano = int(periodo[:4])
                # SOMATORIA
                if int(mes) == 12:
                    mes = meses[0]
                    ano += 1
                else:
                    mes = meses[mes]
                periodo = str(ano) + '-' + str(mes)
        def remover_mes_atual(periodo):
            saida.delete()
            # atualizar dashboard
            func_dashboard(periodo = periodo)
        
        verifica = request.POST.get('remover_mes_em_diante', False)

        if verifica:
            remover_mes_em_diante(saida.periodo)
        else:
            remover_mes_atual(saida.periodo)
        return redirect('mostra_entrada_saida')
    return render(request, 'confirma_remover.html', {'saida': saida})

