from django.urls import path
from .views import home, deletar, atualizar, pesquisar, criar

urlpatterns = [
    path('', home, name="home"),

    path('pesquisar/', pesquisar, name="pesquisar"),
    path('deletar', deletar, name="deletar"),
    path('deletar/<int:id>', deletar, name="deletar_id"),
    path('criar', criar, name="criar"),

    path('atualizar/<int:id>', atualizar, name="atualizar_id"),
    path('atualizar/', atualizar, name="atualizar")

]
