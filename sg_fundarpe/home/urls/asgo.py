from django.contrib import admin
from django.urls import path
from home.views.asgo import cadastrar_empenho, homepage

urlpatterns = [
    path('', homepage, name='asgo'),
    path('cadastrar_empenho/', cadastrar_empenho, name='cadastrar_empenho'),
]