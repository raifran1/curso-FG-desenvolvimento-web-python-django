from django.shortcuts import render
from .models import Postagem
# Create your views here.

def home(request):
    posts = Postagem.objects.filter(status='Publicado')
    return render(request, 'postagem/home.html', locals())

def contato(request):
    return render(request, 'postagem/contato.html', locals())

def postagens_autor(request, id):
    posts = Postagem.objects.filter(autor__id=id)
    return render(request, 'postagem/postagens_autor.html', locals())

def postar(request):
    return render(request, 'postagem/postar.html', locals())

