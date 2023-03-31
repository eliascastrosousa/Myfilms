from django.contrib import admin
from django.urls import path, include
from .views import home, criaritem, salvar

urlpatterns = [
    path('', home, name="index"),
    path('criaritem/', criaritem, name="criaritem"),
    path('salvar/', salvar, name="salvar"),

    

]
