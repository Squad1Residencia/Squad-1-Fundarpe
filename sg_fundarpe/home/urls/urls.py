from django.contrib import admin
from django.urls import path, include
from .views import homepage, salvar, editar, atualizar,deletar

urlpatterns = [
   path('', homepage, name = 'home'),
   path('salvar/', salvar, name = 'salvar'),
   path('editar/<int:n_projeto>', editar, name = 'editar'),
   path('atualizar/<int:n_projeto>', atualizar, name = 'atualizar'),
   path('deletar/<int:n_projeto>', deletar, name = 'deletar')
]
