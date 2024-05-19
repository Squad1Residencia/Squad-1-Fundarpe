from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse, JsonResponse 
from home.models import Projeto, Pagamento, Operacao
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone


@login_required
def homepage(request):
    # Verificar se o usuário pertence ao departamento 'unat'
    if request.user.departamento != 'unat':
        return HttpResponseForbidden()

    projetos = Projeto.objects.all() 
    return render(request, 'home/unat.html', {'projetos': projetos})

@login_required
@login_required
def cadastrar_projeto(request):
    if request.method == 'POST':
        # Obtém os dados do formulário
        n_projeto = request.POST.get('n_projeto')
        titulo_projeto = request.POST.get('titulo_projeto')
        n_sei = request.POST.get('n_sei')
        valor_solicitado = request.POST.get('valor_solicitado')
        n_parcelas = request.POST.get('n_parcelas')

        # Verificar se um projeto com o mesmo n_projeto já existe
        projeto, created = Projeto.objects.get_or_create(
            n_projeto=n_projeto,
            defaults={'titulo_projeto': titulo_projeto, 'n_sei': n_sei, 'status_projeto': '1'},
        )

        # Se o projeto já existir, atualizar os dados
        if not created:
            projeto.titulo_projeto = titulo_projeto
            projeto.n_sei = n_sei
            projeto.status_projeto = '1'
            projeto.save()

        # Criar uma nova Operacao
        operacao = Operacao()
        operacao.n_projeto = projeto
        operacao.id_usuario = request.user
        operacao.status_operacao = 'Editado' if not created else 'Criado'
        operacao.nome_operacao = 'Projeto Editado' if not created else 'Projeto Criado'
        operacao.data_operacao = timezone.now()  # Definindo data_operacao como a data atual
        operacao.save()

        novo_pagamento, created = Pagamento.objects.get_or_create(
            n_projeto=projeto,
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
    
