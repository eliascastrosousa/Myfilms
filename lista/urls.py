from django.contrib import admin
from django.urls import path, include
from .views import home, criaritem, salvar,update, delete,editar, excluir,detalhes, perfil, login, register

urlpatterns = [
    path('', home, name="index"),
    path('criaritem', criaritem, name="criaritem"),
    path('salvar/', salvar, name="salvar"),
    path('detalhes/<int:id>', detalhes, name="detalhes"),
    path('editar/<int:id>', editar, name="editar"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('excluir/<int:id>', excluir, name="excluir"),
    path('perfil', perfil, name="perfil"),
    path('login', login, name="login"),
    path('register', register, name="register")

    

]
