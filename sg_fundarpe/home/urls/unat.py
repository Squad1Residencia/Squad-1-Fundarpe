from django.contrib import admin
from django.urls import path
from home.views.unat import homepage, cadastrar_projeto, atualizar_projeto

urlpatterns = [
      path('', homepage, name = 'unat'),
      path('cadastrar/', cadastrar_projeto, name = 'cadastrar_projeto'),
      path('atualizar/<int:n_projeto>', atualizar_projeto, name = 'atualizar_projeto'),
]       