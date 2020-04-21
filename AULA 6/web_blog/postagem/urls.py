from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('sobre-nos/', contato, name='contato'),
    path('postagens/autor/<int:id>/', postagens_autor, name='postagens_autor'),
    path('postar/', postar, name='postar'),
    path('deletar/<int:id_post>/', deletar_post, name='deletar_post'),
    path('editar/<int:id_post>/', editar_post, name='editar_post')
]