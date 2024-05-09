from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.precisa_redefinir_senha:
                return redirect('redefinir_senha')
            else:
                # Obter o departamento do usuário
                departamento = user.departamento
                # Redirecionar para a página inicial do departamento
                return redirect(f'/{departamento}/')
        else:
            # Retornar um erro 'invalid login'
            return render(request, 'login.html', {'error': 'Login inválido'})
    else:
        return render(request, 'login.html')
    

def redefinir_senha_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            nova_senha = request.POST['nova_senha']
            confirmar_senha = request.POST['confirmar_senha']

            # Validação da senha
            if nova_senha != confirmar_senha:
                return render(request, 'redefinir_senha.html', {'error': 'As senhas não correspondem'})
            if len(nova_senha) < 8:
                return render(request, 'redefinir_senha.html', {'error': 'A senha deve ter pelo menos 8 caracteres'})

            # Alterar a senha do usuário
            request.user.set_password(nova_senha)
            request.user.precisa_redefinir_senha = False
            request.user.save()
            update_session_auth_hash(request, request.user)  # Atualiza a sessão para manter o usuário logado após a alteração da senha
            return redirect('login')  # Redireciona para a página de login
    else:
        return render(request, 'redefinir_senha.html')