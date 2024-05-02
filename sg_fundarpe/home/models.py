from django.db import models

class Projeto(models.Model):
    n_projeto = models.IntegerField(primary_key=True)
    titulo_projeto = models.TextField()
    n_sei = models.IntegerField()
    n_empenho = models.CharField(max_length=255)
    data_solicitacao = models.DateField()
    status_projeto = models.CharField(max_length=255)
    n_termoaceite = models.CharField(max_length=255)
    reponsavel_termo = models.CharField(max_length=255)

class Usuario(models.Model):
    id_usuario = models.CharField(max_length=255, primary_key=True)
    senha = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)

class Operacao(models.Model):
    id_operacao = models.IntegerField(primary_key=True)
    n_projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_operacao = models.DateField()
    status_operacao = models.CharField(max_length=255)
    nome_operacao = models.CharField(max_length=255)

class Pagamento(models.Model):
    n_projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    valor_solicitado = models.DecimalField(max_digits=10, decimal_places=2)
    n_parcelas = models.PositiveSmallIntegerField()
    status_pagamento = models.TextField()
    descricao = models.TextField()