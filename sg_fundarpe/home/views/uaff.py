from django.shortcuts import render, redirect
from home.models import Projeto, Operacao #chamar tabelas que serão utilizadas
from django.http import HttpResponse

def homepage(request):
    projetos = Projeto.objects.all() 
    return render(request, 'home/uaff.html', {'projetos': projetos})

def cadastro_uaff(request):
    if request.method == 'POST':
        # Obtém os dados do formulário
        n_projeto = request.POST.get('n_projeto')
        nome_operacao = request.POST.get('nome_operacao')
        data_operacao = request.POST.get('data_operacao')
        
        projeto = Projeto.objects.filter(n_projeto=n_projeto).first()
        if not projeto:
            return HttpResponse("Projeto não encontrado", status=400)

        # Define o status do projeto com base na operação
        if nome_operacao == 'Conferência da Documentação':
            projeto.status_projeto = '2'
        elif nome_operacao == 'Envio para Confecção do Termo':
            projeto.status_projeto = '5'

        projeto.save()
        Operacao.objects.create(n_projeto=projeto, id_usuario=request.user, data_operacao=data_operacao, status_operacao='Concluida', nome_operacao=nome_operacao)
        return redirect('uaff')
    else:
        return HttpResponse("Erro ao cadastrar a operação", status=400)
    
def cadastro_uaff1(request):
    if request.method == 'POST':
        # Obtém os dados do formulário
        n_projeto = request.POST.get('n_projeto')
        nome_operacao = request.POST.get('nome_operacao')
        data_envio = request.POST.get('data_envio')
        data_recebimento = request.POST.get('data_recebimento')
        nome_envio = request.POST.get('nome_envio')
        
        projeto = Projeto.objects.filter(n_projeto=n_projeto).first()
        if not projeto:
            return HttpResponse("Projeto não encontrado", status=400)

        # Define o status do projeto para a terceira operação
        if nome_operacao == 'Recebimento doc assinado':
            projeto.status_projeto = '8'

        projeto.save()
        # Resto do código...
        Operacao.objects.create(n_projeto=projeto, id_usuario=request.user, status_operacao='Concluida', nome_operacao=nome_operacao,data_operacao=data_recebimento)
        Operacao.objects.create(n_projeto=projeto, id_usuario=request.user, status_operacao='Concluida',data_operacao=data_envio,nome_operacao=nome_envio )
        return redirect('uaff')
    else:
        return HttpResponse("Erro ao cadastrar a operação", status=400)