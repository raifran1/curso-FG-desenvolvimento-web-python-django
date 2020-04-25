from django.urls import path
from .views import *
from autor.views import cadastro_autor, editar_autor

urlpatterns = [
    path('cadastro/autor/', cadastro_autor, name='cadastro_autor'),
    path('concluir/cadastro/?P<int:id_autor>/', add_user, name='add_user'),
    path('login-usuario/', user_login, name='user_login'),
    path('logout-usuario/', user_logout, name='user_logout'),
    path('alterar-senha', alterar_senha, name='alterar_senha'),
    path('editar-user', editar_user, name='editar_user'),
    path('editar-autor', editar_autor, name='editar_autor')
]