from django.shortcuts import render, redirect
from .models import Lista

def home(request):
    v_lista = Lista.objects.all()
    return render(request, 'index.html', {"lista":v_lista})

def criaritem(request):
    return render(request, 'criaritem.html')

def salvar(request):
    v_nome = request.POST.get("nome")
    v_tipo_filme = request.POST.get("tipo_filme")
    
    if request.POST.get("concluido"):
        v_concluido = True
    else:
        v_concluido = False

    v_resenha =  request.POST.get("resenha")
    v_lista = Lista.objects.all()
    Lista.objects.create(nome=v_nome, tipo_filme = v_tipo_filme, concluido = v_concluido, resenha = v_resenha )
    return render(request, 'index.html', {"lista":v_lista})

def editar(request, id):
    lista  = Lista.objects.get(id=id)
    return render(request, 'update.html', {'lista':lista})

def update(request, id):
    v_nome = request.POST.get("nome")
    v_tipo_filme = request.POST.get("tipo_filme")
    if request.POST.get("concluido"):
        v_concluido = True
    else:
        v_concluido = False
    v_resenha =  request.POST.get("resenha")
    lista = Lista.objects.get(id=id)
    lista.nome = v_nome
    lista.tipo_filme = v_tipo_filme
    lista.concluido = v_concluido
    lista.resenha = v_resenha
    lista.save()
    return redirect(home)   

def delete(request, id):
    lista = Lista.objects.get(id=id)
    return render(request, 'delete.html', {"lista":lista})

def excluir(request, id):
    lista = Lista.objects.get(id=id)
    lista.delete()
    return redirect(home)

def detalhes(request, id):
    lista = Lista.objects.get(id=id)
    return render(request, 'detalhes.html', {"lista":lista})