from django.urls import path
from .views import home, adicionar_entrada, alterar_entrada, remover_entrada


urlpatterns = [
    path('', home, name='mostra_entrada_saida'),
    path('adicionar/entrada/', adicionar_entrada, name='adicionar_entrada'),
    path('alterar/entrada/<int:id>/', alterar_entrada, name='alterar_entrada'),
    path('remover/entrada/<int:id>/', remover_entrada, name='remover_entrada'),
]
