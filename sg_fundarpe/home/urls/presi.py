from django.contrib import admin
from django.urls import path
from home.views.presi import cadastrar_operacao, homepage

urlpatterns = [
       path('', homepage, name = 'presi'),
       path('cadastro_operacao/', cadastrar_operacao, name = 'cadastro_operacao'),
]          