from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Usuario(AbstractUser):
    id_usuario = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=255)
    precisa_redefinir_senha = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, related_name='usuario_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='usuario_permissions', blank=True)

    def __str__(self):
        return str(self.id_usuario)
    
class Projeto(models.Model):
    n_projeto = models.IntegerField(primary_key=True)
    titulo_projeto = models.TextField()
    n_sei = models.IntegerField()
    n_empenho = models.CharField(max_length=255, null=True)
    data_solicitacao = models.DateField(null=True)
    status_projeto = models.CharField(max_length=255, null=True)
    n_termoaceite = models.CharField(max_length=255, null=True)
    reponsavel_termo = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.titulo_projeto

class Operacao(models.Model):
    id_operacao = models.AutoField(primary_key=True)
    n_projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_operacao = models.DateField()
    status_operacao = models.CharField(max_length=255)
    nome_operacao = models.CharField(max_length=255)
    data_cadastro = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.nome_operacao

class Pagamento(models.Model):
    n_projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    valor_solicitado = models.DecimalField(max_digits=10, decimal_places=2)
    n_parcelas = models.PositiveSmallIntegerField()
    status_pagamento = models.TextField(null=True)
    descricao = models.TextField(null=True)

    def __str__(self):
        return self.n_projeto.titulo_projeto
    
