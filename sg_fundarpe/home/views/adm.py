from django.shortcuts import render, redirect
from home.models import Projeto #chamar tabelas que serão utilizadas
from django.http import HttpResponse

def homepage(request):
    projetos = Projeto.objects.all() 
    return render(request, 'home/adm.html', {'projetos': projetos})
