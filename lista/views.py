from django.shortcuts import render
from .models import Lista

def home(request):
    v_lista = Lista.objects.all()
    return render(request, 'index.html', {"lista":v_lista})

def criaritem(request):
    return render(request, 'criaritem.html')

def salvar(request):
    v_nome = request.POST.get("nome")
    v_tipo_filme = request.POST.get("tipo_filme")
    v_concluido =  request.POST.get("concluido")
    v_resenha =  request.POST.get("resenha")
    v_lista = Lista.objects.all()
    Lista.objects.create(nome=v_nome, tipo_filme = v_tipo_filme, concluido = v_concluido, resenha = v_resenha )
    return render(request, 'index.html', {"lista":v_lista})
