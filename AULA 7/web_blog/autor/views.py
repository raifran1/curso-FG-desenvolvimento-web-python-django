from django.shortcuts import render, redirect
from autor.forms import AutorForm


def cadastro_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_user', form.id)
        else:
            print(form.errors)
    else:
        form = AutorForm()
    return render(request, 'autor/cadastrar_autor.html', locals())