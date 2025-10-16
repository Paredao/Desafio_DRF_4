from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nome

class Chamado(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    usuario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        related_name='chamados'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo