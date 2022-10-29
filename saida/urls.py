from django.urls import path
from .views import adicionar_saida, alterar_saida, remover_saida


urlpatterns = [
    path('adicionar/saida/', adicionar_saida, name='adicionar_saida'),
    path('alterar/saida/<int:id>/', alterar_saida, name='alterar_saida'),
    path('remover/saida/<int:id>/', remover_saida, name='remover_saida'),
]
