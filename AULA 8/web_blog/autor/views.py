from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from autor.forms import AutorForm
from django.contrib import messages

from .models import Autor


def cadastro_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('add_user', f.id)
        else:
            print(form.errors)
            messages.error(request, form.errors)
    else:
        form = AutorForm()
    return render(request, 'autor/cadastrar_autor.html', locals())


@login_required
def editar_autor(request):
    usuario = User.objects.get(id=request.user.id)
    autor = Autor.objects.get(email=usuario.email)
    if request.method == 'POST':
        form = AutorForm(data=request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = AutorForm(instance=autor)
    return render(request, 'autor/editar_autor.html', locals())