from django.db import models

# Create your models here.
FORMACAO_CHOICES = (('Ens. Médio', ('Ens. Médio')),
                   ('Superior Incompleto', ('Superior Incompleto')),
                   ('Superior Completo', ('Superior Completo')))

class Curriculo(models.Model):
    nome = models.CharField(max_length=500, verbose_name='Nome Completo')
    idade = models.PositiveIntegerField(verbose_name='Idade')
    formacao = models.CharField(verbose_name='Formação', max_length=30, choices=FORMACAO_CHOICES)

    class Meta:
        verbose_name = "Currículo"
        verbose_name_plural = "Curriculos"

    def __str__(self):
        return self.nome

