from django.contrib import admin
from django.urls import path
from home.views.seju import *

urlpatterns = [
       path('', homepage, name = 'seju'),
       path('cadastrar_seju/', cadastrar_operacao, name = 'cadastrar_seju'),

]       
