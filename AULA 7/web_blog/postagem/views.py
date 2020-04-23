from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Postagem
from .forms import PostagemForm
from autor.models import Autor
from django.contrib.auth.models import User

def home(request):
    posts = Postagem.objects.filter(status='Publicado')
    return render(request, 'postagem/home.html', locals())

def contato(request):
    return render(request, 'postagem/contato.html', locals())

def postagens_autor(request, id):
    posts = Postagem.objects.filter(autor__id=id)
    return render(request, 'postagem/postagens_autor.html', locals())

@login_required
def postar(request):
    usuario = User.objects.get(id=request.user.id)
    autor = Autor.objects.get(email=usuario.email)
    # metodos http: GET, POST, PUCH, DELETE
    if request.method == 'POST':
        form = PostagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postagens_autor', autor.id)
        else:
            print(form.errors)
    else:
        form = PostagemForm()
    data = datetime.now()
    return render(request, 'postagem/postar.html', locals())

def deletar_post(request, id_post):
    post = get_object_or_404(Postagem, id=id_post)
    usuario = User.objects.get(id=request.user.id)
    autor = Autor.objects.get(email=usuario.email)
    post.delete()
    return redirect('postagens_autor', autor.id)

def editar_post(request, id_post):
    usuario = User.objects.get(id=request.user.id)
    autor = Autor.objects.get(email=usuario.email)
    post = Postagem.objects.get(id=id_post)
    # metodos http: GET, POST, PUCH, DELETE
    if request.method == 'POST':
        form = PostagemForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('postagens_autor', autor.id)
        else:
            print(form.errors)
    else:
        form = PostagemForm(instance=post)
    data = datetime.now()
    return render(request, 'postagem/postar.html', locals())
