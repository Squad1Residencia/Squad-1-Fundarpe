from django.shortcuts import render, redirect
from ..models import Projeto
#from .forms import ProjetoForm


def homepage(request):
    projetos = Projeto.objects.all() 
    return render(request, 'home/index.html', {'projetos': projetos})


#Implementacao do Create do Crud
def salvar(request):
    n_projeto = request.POST.get('n_projeto')
    titulo_projeto = request.POST.get('titulo_projeto')
    n_sei = request.POST.get('n_sei')
    n_empenho = request.POST.get('n_empenho')
    data_solicitacao = request.POST.get('data_solicitacao')
    status_projeto = request.POST.get('status_projeto')
    n_termoaceite = request.POST.get('n_termoaceite')
    reponsavel_termo = request.POST.get('responsavel_termo')

    Projeto.objects.create(n_projeto = n_projeto, titulo_projeto = titulo_projeto, n_sei = n_sei, n_empenho = n_empenho, data_solicitacao = data_solicitacao, status_projeto = status_projeto, n_termoaceite = n_termoaceite, reponsavel_termo = reponsavel_termo)
    
    projetos = Projeto.objects.all() 
    return  render(request, 'home/index.html', {'projetos': projetos})

def editar(request, n_projeto):
    projeto = Projeto.objects.get(n_projeto = n_projeto)
    return render(request, 'home/editar.html', {'projeto': projeto})


#Implementacao do update
def atualizar(request, n_projeto):
    projeto = Projeto.objects.get(n_projeto=n_projeto)
    projeto.titulo_projeto = request.POST.get('titulo_projeto')
    projeto.n_sei = request.POST.get('n_sei')
    projeto.n_empenho = request.POST.get('n_empenho')
    projeto.data_solicitacao = request.POST.get('data_solicitacao')
    projeto.status_projeto = request.POST.get('status_projeto')
    projeto.n_termoaceite = request.POST.get('n_termoaceite')
    projeto.reponsavel_termo = request.POST.get('responsavel_termo')
    projeto.save()
    return redirect('home')

def deletar(request, n_projeto):
    projeto = Projeto.objects.get(n_projeto=n_projeto)
    projeto.delete()
    return redirect('home')