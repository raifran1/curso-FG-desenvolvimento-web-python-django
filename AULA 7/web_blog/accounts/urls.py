from django.urls import path
from .views import *
from autor.views import cadastro_autor

urlpatterns = [
    path('cadastro/autor/', cadastro_autor, name='cadastro_autor'),
    path('concluir/cadastro/?P<int:id_autor>/', add_user, name='add_user'),
    path('login-usuario/', user_login, name='user_login'),
    path('logout-usuario/', user_logout, name='user_logout'),
]