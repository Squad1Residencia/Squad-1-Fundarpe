from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse, JsonResponse 
from home.models import Projeto, Pagamento
from django.shortcuts import render, redirect, get_object_or_404

@login_required
def homepage(request):
    # Verificar se o usuário pertence ao departamento 'unat'
    if request.user.departamento != 'unat':
        return HttpResponseForbidden()

    projetos = Projeto.objects.all() 
    return render(request, 'home/unat.html', {'projetos': projetos})

@login_required
def cadastrar_projeto(request):
    # Verificar se o usuário pertence ao departamento 'unat'
    if request.user.departamento != 'unat':
        return HttpResponseForbidden()

    if request.method == 'POST':
        n_projeto = request.POST.get('n_projeto')
        titulo_projeto = request.POST.get('titulo_projeto')
        n_sei = request.POST.get('n_sei')
        valor_solicitado = request.POST.get('valor_solicitado')
        n_parcelas = request.POST.get('n_parcelas')

        novo_projeto, created = Projeto.objects.get_or_create(
            n_projeto=n_projeto,
            defaults={'titulo_projeto': titulo_projeto, 'n_sei': n_sei},
        )

        if not created:
            novo_projeto.titulo_projeto = titulo_projeto
            novo_projeto.n_sei = n_sei
            novo_projeto.save()

        novo_pagamento, created = Pagamento.objects.get_or_create(
            n_projeto=novo_projeto,
            defaults={'valor_solicitado': valor_solicitado, 'n_parcelas': n_parcelas},
        )

        if not created:
            novo_pagamento.valor_solicitado = valor_solicitado
            novo_pagamento.n_parcelas = n_parcelas
            novo_pagamento.save()

        return redirect('unat')
    else:
        return HttpResponse("Erro ao cadastrar o projeto", status=400)

@login_required
def editar_projeto(request, n_projeto):
    # Busca o projeto com base no n_projeto
    projeto = get_object_or_404(Projeto, n_projeto=n_projeto)

    # Busca o pagamento associado ao projeto
    pagamento = get_object_or_404(Pagamento, n_projeto=projeto)

    # Cria um dicionário com os dados do projeto e do pagamento
    data = {
        'n_projeto': projeto.n_projeto,
        'titulo_projeto': projeto.titulo_projeto,
        'n_sei': projeto.n_sei,
        'valor_solicitado': pagamento.valor_solicitado,
        'n_parcelas': pagamento.n_parcelas,
    }

    # Retorna os dados como JSON
    return JsonResponse(data)
    