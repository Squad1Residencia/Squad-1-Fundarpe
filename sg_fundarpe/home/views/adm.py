from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from home.models import Usuario, Projeto, Operacao, Pagamento

def homepage(request):
    projetos = Projeto.objects.all()
    users = Usuario.objects.all()
    operacoes = Operacao.objects.all()
    pagamentos = Pagamento.objects.all()
    for pagamento in pagamentos:
        print(pagamento)
    return render(request, 'home/adm.html', {'users': users, 'operações': operacoes, 'projetos': projetos, 'pagamentos': pagamentos})

