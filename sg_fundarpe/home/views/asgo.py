from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect
from home.models import Projeto, Operacao 
from datetime import datetime

# @login_required
def homepage(request):
    # Verificar se o usuário pertence ao departamento 'asgo'
    # if request.user.departamento != 'asgo':
    #     return redirect('/login/')

    projetos = Projeto.objects.filter(n_empenho__isnull=True)  
    return render(request, 'home/asgo.html', {'projetos': projetos})

# @login_required
def cadastrar_empenho(request):
    if request.method == 'POST':
        # Obtém os dados do formulário
        n_projeto = request.POST.get('n_projeto')
        n_empenho = request.POST.get('n_empenho')

        # Verifica se um projeto com o mesmo n_projeto existe
        projeto = Projeto.objects.filter(n_projeto=n_projeto).first()
        if not projeto:
            return HttpResponse("Um projeto com esse número não existe", status=400)
        
        # Atualiza o n_empenho do projeto e cria uma nova operação
        projeto.n_empenho = n_empenho
        projeto.status_projeto = '4'  # Adiciona o status do projeto
        projeto.save()
        Operacao.objects.create(n_projeto=projeto, id_usuario=request.user, data_operacao=datetime.now(), status_operacao='Concluida', nome_operacao='Cadastro de Empenho')
        return redirect('asgo')
    else:
        return HttpResponse("Erro ao cadastrar o empenho", status=400)