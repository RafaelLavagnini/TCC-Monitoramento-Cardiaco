from usuarios.forms import LoginForms, CadastroForms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from usuarios.models import Perfil
from monitoramento.models import Fotografia

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['nome_login']
            password = form.cleaned_data['senha']

            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                Fotografia.objects.filter(usuario=user).update(publicada=1)

                Fotografia.objects.exclude(usuario=user).update(publicada=0)

                return redirect('index')
            else:
                messages.error(request, 'Usuário e/ou senha incorreto(s)!')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                messages.error(request, 'Senhas não são iguais')
                return redirect('cadastro')

            nome = form.cleaned_data['nome_cadastro']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha_1']
            categoria = form.cleaned_data['categoria']

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            
            perfil = Perfil.objects.create(user=usuario, categoria=categoria)
            perfil.save()

            Fotografia.objects.filter(categoria=categoria).update(usuario=usuario, publicada=True)

            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    if request.user.is_authenticated:
        Fotografia.objects.filter(usuario=request.user).update(publicada=False)
        auth.logout(request)

    return redirect('login')
