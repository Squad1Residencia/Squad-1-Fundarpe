from django.contrib import admin
from django.urls import path
from home.views.unat import homepage, cadastrar_projeto, editar_projeto

urlpatterns = [
       path('', homepage, name = 'unat'),
       path('cadastrar/', cadastrar_projeto, name = 'cadastrar_projeto'),
      path('editar/<int:n_projeto>', editar_projeto, name = 'editar_projeto'),
]       