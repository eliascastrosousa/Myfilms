from django.contrib import admin
from django.urls import path, include
from .views import home, criaritem, salvar,update, delete,editar, excluir

urlpatterns = [
    path('', home, name="index"),
    path('criaritem', criaritem, name="criaritem"),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:id>', editar, name="editar"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('excluir/<int:id>', excluir, name="excluir"),

    

]
