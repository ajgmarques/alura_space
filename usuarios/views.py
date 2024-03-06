from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid:
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'Usuário {nome} logado com sucesso')
                return redirect('index')
            else:
                messages.error(request, 'Nome ou senha inválida!!')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})


def logout(request):
    # usuario_logado = request.user
    if not request.user.is_authenticated:
        messages.error(request, 'Não há usuários logados')
        return redirect('login')
    else:
        auth.logout(request)
        messages.success(request, 'Logout efetuado com sucesso')
        return redirect('login')


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form['senha_usuario'].value() != form['senha_usuario_confirma'].value():
                messages.error(request, 'As senhas não são iguais!')
                return redirect('cadastro')

            nome = form['nome_usuario'].value()
            email = form['email_usuario'].value()
            senha = form['senha_usuario'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existe!')
                return redirect('cadastro')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email já existe!')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(
                request,
                f'O usuário {nome} foi cadastrado com sucesso'
            )
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})
