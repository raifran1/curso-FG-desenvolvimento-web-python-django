from django.contrib.auth import authenticate, login, logout
from django.core.checks import messages
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserForm
from autor.models import Autor


def add_user(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid(): ## last_name = 'Raifran', email='contato@raifranlucas.dev', username='raifran', password='1234'
            var = form.save()
            var.set_password(var.password)
            var.username = var.email
            var.save()
        else:
            print(form.errors)
            messages.ERROR(request, form.errors)
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
            messages.ERROR(request, 'Usuário ou senha inválidos ou desativados. ')
    return render(request, 'accounts/login.html', locals())


def user_logout(request):
    logout(request)
    return redirect('home')