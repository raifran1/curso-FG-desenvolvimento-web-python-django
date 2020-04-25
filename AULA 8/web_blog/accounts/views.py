from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserForm
from autor.models import Autor


def add_user(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid(): ## last_name = 'Raifran', email='contato@raifranlucas.dev', username='raifran', password='1234'

            var = form.save(commit=False)
            var.set_password(var.password)
            var.email = var.username
            var.save()

            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        else:
            print(form.errors)
            messages.error(request, form.errors)
    else:
        form = UserForm()
    return render(request, 'accounts/add_user.html', locals())


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            print(messages.ERROR)
            messages.error(request, 'Usuário ou senha inválidos ou desativados. ')
    return render(request, 'accounts/login.html', locals())


def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def alterar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            #messages.success(request, 'Senha alterada com sucesso')
            return redirect('home')
        else:
            messages.error(request, form.errors)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/alterar_senha.html', locals())

@login_required
def editar_user(request):
    usuario = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = UserForm(instance=usuario)
    return render(request, 'accounts/editar_user.html', locals())
