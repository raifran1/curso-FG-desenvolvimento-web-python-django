from django.db import models

# Create your models here.
STATUS_CHOICE = (('Rascunho', ('Rascunho')),
                 ('Publicado', ('Publicado')))
class Postagem(models.Model):
    autor = models.ForeignKey('autor.Autor', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=60)
    conteudo = models.TextField()
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_publicacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICE)

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

    def __str__(self):
        return self.titulo