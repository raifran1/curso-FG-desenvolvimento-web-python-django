from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'postagem/home.html', locals())

def contato(request):
    return render(request, 'postagem/contato.html', locals())

def postagens_autor(request):
    return render(request, 'postagem/postagens_autor.html', locals())

def postar(request):
    return render(request, 'postagem/postar.html', locals())

