from django.shortcuts import render, redirect
from home.models import Projeto, Pagamento
from django.http import HttpResponse


def homepage(request):
    projetos = Projeto.objects.all() 
    return render(request, 'home/unat.html', {'projetos': projetos})


def cadastrar_projeto(request):
    if request.method == 'POST':
        n_projeto = request.POST.get('n_projeto')
        titulo_projeto = request.POST.get('titulo_projeto')
        n_sei = request.POST.get('n_sei')
        valor_solicitado = request.POST.get('valor_solicitado')
        n_parcelas = request.POST.get('n_parcelas')

        novo_projeto = Projeto.objects.create(n_projeto=n_projeto, titulo_projeto=titulo_projeto, n_sei=n_sei)
        novo_pagamento = Pagamento.objects.create(n_projeto=novo_projeto, valor_solicitado=valor_solicitado, n_parcelas=n_parcelas)
        
        return redirect('unat')
    else:
        return HttpResponse("Erro ao cadastrar o projeto", status=400)
    
def atualizar_projeto(request, n_projeto):
    if request.method == 'POST':
        n_projeto = request.POST.get('n_projeto')
        titulo_projeto = request.POST.get('titulo_projeto')
        n_sei = request.POST.get('n_sei')
        valor_solicitado = request.POST.get('valor_solicitado')
        n_parcelas = request.POST.get('n_parcelas')

        projeto = Projeto.objects.get(id=n_projeto)
        projeto.n_projeto = n_projeto
        projeto.titulo_projeto = titulo_projeto
        projeto.n_sei = n_sei
        projeto.save()

        pagamento = Pagamento.objects.get(n_projeto_id=n_projeto)
        pagamento.valor_solicitado = valor_solicitado
        pagamento.n_parcelas = n_parcelas
        pagamento.save()

        return redirect('unat')
    else:
        return HttpResponse("Erro ao atualizar o projeto", status=400)
