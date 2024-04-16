from django.urls import path
from .views import home, produtos, precos, deletar, atualizar

urlpatterns = [
    path('', home, name="home"),

    path('deletar/<int:id>', deletar, name="deletar"),
    path('atualizar/<int:id>', atualizar, name="atualizar"),

    path('produtos/', produtos),
    path('precos/', precos),
    path('precos/<int:id>', precos),
]
