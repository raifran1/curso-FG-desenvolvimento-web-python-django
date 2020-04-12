from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('sobre-nos/', contato, name='contato'),
    path('postagens/autor/', postagens_autor, name='postagens_autor'),
    path('postar/', postar, name='postar'),
]