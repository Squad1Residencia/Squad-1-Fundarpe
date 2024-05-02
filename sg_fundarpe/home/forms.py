
'''
Pesquisar mais sobre django forms

from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['n_projeto', 'titulo_projeto', 'n_sei', 'n_empenho', 'data_solicitacao', 'status_projeto', 'n_termoaceite', 'reponsavel_termo']

        
'''

