from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect
from home.models import Projeto, Operacao 
from datetime import datetime

#@login_required
def homepage(request):
    # Verificar se o usuário pertence ao departamento 'asgo'
    #if request.user.departamento != 'asgo':
        #return HttpResponseForbidden()

    projetos = Projeto.objects.all() 
    return render(request, 'home/asgo.html', {'projetos': projetos})

#@login_required
def cadastrar_empenho(request):
  
    #if request.user.departamento != 'asgo':
        #return HttpResponseForbidden()
    
    if request.method == 'POST':
        # Obtém os dados do formulário
        n_projeto = request.POST.get('n_projeto')
        n_empenho = request.POST.get('n_empenho')

        # Verifica se um projeto com o mesmo n_projeto existe
        projeto = Projeto.objects.filter(n_projeto=n_projeto).first()
        if not projeto:
            return HttpResponse("Um projeto com esse número não existe", status=400)
        
        # Verifica se um empenho com o mesmo n_empenho já existe
        #if projeto.n_empenho:
            #return HttpResponse("Um empenho com esse número já existe", status=400)
        
        # Atualiza o n_empenho do projeto e cria uma nova operação
        projeto.n_empenho = n_empenho
        projeto.save()
        Operacao.objects.create(n_projeto=projeto, id_usuario=request.user, data_operacao=datetime.now(), status_operacao='Concluida', nome_operacao='Cadastro de Empenho')
        return redirect('asgo')
    else:
        return HttpResponse("Erro ao cadastrar o empenho", status=400)