from django.contrib import admin
from django.urls import path
from home.views.asju import *

urlpatterns = [
       path('', homepage, name = 'asju'),
       path('cadastrar_asju/', cadastrar_operacao, name = 'cadastrar_asju'),
]       
