from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Count, F
from home.models import Usuario, Projeto, Operacao, Pagamento, Usuario
from django.http import JsonResponse

# @login_required
def homepage(request):
    # if request.user.departamento != 'adm':
    #     return redirect('/login/')
    projetos = Projeto.objects.all()
    users = Usuario.objects.all()
    pagamentos = Pagamento.objects.all()
    operacoes = Operacao.objects.all()

# Crie uma lista para armazenar os dados do usuário
    dados_usuario = []

# Para cada usuário, obtenha suas operações e o número total de operações
    for usuario in Usuario.objects.all():
        operacoes_usuario = operacoes.filter(id_usuario=usuario)
        numero_operacoes = operacoes_usuario.count()
        dados_usuario.append({
            'usuario': usuario,
            'operacoes': operacoes_usuario,
            'numero_operacoes': numero_operacoes,
        })


 
    # Calcular os dados para os gráficos
    valor_pago = sum(pagamento.valor_solicitado / pagamento.n_parcelas * pagamento.n_parcelas_pagas for pagamento in pagamentos)
    valor_a_ser_pago = sum((pagamento.valor_solicitado - (pagamento.valor_solicitado / pagamento.n_parcelas * pagamento.n_parcelas_pagas)) for pagamento in pagamentos)
    parcelas_concluidas = sum(pagamento.n_parcelas_pagas for pagamento in pagamentos)
    parcelas_em_andamento = sum(pagamento.n_parcelas - pagamento.n_parcelas_pagas for pagamento in pagamentos)
    projetos_concluidos = pagamentos.filter(status_pagamento='Concluído').count()
    projetos_em_andamento = pagamentos.filter(status_pagamento='Em Andamento').count()
 
    print(projetos_concluidos, projetos_em_andamento, parcelas_concluidas, parcelas_em_andamento)
    return render(request, 'home/adm.html', {
        'users': users, 
        'operacoes': operacoes,
        'projetos': projetos, 
        'pagamentos': pagamentos,
        'valor_pago': valor_pago,
        'valor_a_ser_pago': valor_a_ser_pago,
        'parcelas_concluidas': parcelas_concluidas,
        'parcelas_em_andamento': parcelas_em_andamento,
        'projetos_concluidos': projetos_concluidos,
        'projetos_em_andamento': projetos_em_andamento,
    })

# @login_required
def projeto(request, n_projeto):
    projeto = get_object_or_404(Projeto, n_projeto=n_projeto)

    status_dict = {
    '1': 'Projeto Cadastrado',
    '2': 'Projeto Conferido',
    '3': 'Empenho Autorizado',
    '4': 'Empenho Confeccionado',
    '5': 'Data para Termo adicionada',
    '6': 'Confecção Termo de Compromisso',
    '7': 'Visto do Termo de Compromisso',
    '8': 'Envio do Termo ao Proponente',
    '9': 'Termo Assinado DIF',
    '10': 'Termo Assinado PRESI',
    '11': 'Envio para Pagamento',
    '12': 'Pagamento Concluído',
    } 

    projeto_dict = {
        'n_projeto': projeto.n_projeto,
        'titulo_projeto': projeto.titulo_projeto,
        'n_sei': projeto.n_sei,
        'n_empenho': projeto.n_empenho,
        'data_solicitacao': projeto.data_solicitacao,
        'status_projeto': status_dict.get(projeto.status_projeto, 'Status desconhecido'),
        'n_termoaceite': projeto.n_termoaceite,
        'reponsavel_termo': projeto.reponsavel_termo,
    }
    return JsonResponse(projeto_dict)



    