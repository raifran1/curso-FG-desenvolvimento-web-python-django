from django.db import models

# Create your models here.
SEXO_CHOICES = (('Masculino', ('Masculino')),
                ('Feminino', ('Feminino')),
                ('Outro', ('Outro')))

OCUPACAO_CHOICES = (('Estudante', ('Estudante')),
                    ('Professor', ('Professor')),
                    ('Pesquisador', ('Pesquisador')))

class Autor(models.Model):
    nome_completo = models.CharField(max_length=150)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=30, choices=SEXO_CHOICES)
    email = models.EmailField(max_length=240, unique=True)
    ocupacao = models.CharField(max_length=50, choices=OCUPACAO_CHOICES)
    resumo_perfil = models.TextField()

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome_completo