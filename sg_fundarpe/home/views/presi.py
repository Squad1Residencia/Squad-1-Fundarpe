from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from home.models import Projeto #chamar tabelas que serão utilizadas
from home.models import Projeto , Operacao , Pagamento  #chamar tabelas que serão utilizadas
from django.http import HttpResponse
from datetime import datetime

# @login_required
def homepage(request):
    # if request.user.departamento != 'presi':
    #     return redirect('/login/')
    projetos = Projeto.objects.all()
    return render(request, 'home/presi.html', {'projetos': projetos})

# @login_required
def cadastrar_operacao(request):
    if request.method == 'POST':
        # Obtém os dados do formulário
        n_projeto = request.POST.get('n_projeto')
        nome_operacao = request.POST.get('nome_operacao')
        data_operacao = request.POST.get('data_operacao')

        projeto = Projeto.objects.filter(n_projeto=n_projeto).first()
        if not projeto:
            return HttpResponse("Projeto não encontrado", status=400)

        projeto.status_projeto = '10'
        projeto.save()
        Operacao.objects.create(n_projeto=projeto, id_usuario=request.user, data_operacao=data_operacao, status_operacao='Concluida', nome_operacao=nome_operacao)
        return redirect('presi')
    else:
        return HttpResponse("Erro ao cadastrar a operação", status=400)