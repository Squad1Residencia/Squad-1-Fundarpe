from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from home.models import Usuario

def homepage(request):
    users = Usuario.objects.all()
    departamentos = ['UNAT', 'UAFF', 'SEJU', 'PRESI', 'DIF', 'ASJU', 'ASGO', 'ADM', 'INATIVO']
    return render(request, 'home/adm.html', {'users': users, 'departamentos': departamentos})

def criar_usuario(request):
    User = get_user_model()
    departamentos = ['UNAT', 'UAFF', 'SEJU', 'PRESI', 'DIF', 'ASJU', 'ASGO', 'ADM', 'INATIVO']
    password = None
    if request.method == 'POST':
        username = request.POST['username']
        departamento = request.POST['departamento'].lower()
        # Gerar uma senha aleatória
        password = User.objects.make_random_password()
        # Criar um novo usuário
        user = User(username=username, departamento=departamento)
        user.set_password(password)
        user.save()
    users = User.objects.all()
    return render(request, 'adm.html', {'users': users, 'password': password, 'departamentos': departamentos})