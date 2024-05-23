from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Projeto, Pagamento, Operacao

class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'departamento', 'precisa_redefinir_senha']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('departamento', 'precisa_redefinir_senha')}),
    )

class OperacaoAdmin(admin.ModelAdmin):
    list_display = ('nome_operacao', 'get_n_projeto', 'get_id_usuario', 'data_operacao')

    def get_n_projeto(self, obj):
        return obj.n_projeto.titulo_projeto
    get_n_projeto.short_description = 'N Projeto'  # Renomeia a coluna no Admin

    def get_id_usuario(self, obj):
        return obj.id_usuario.username
    get_id_usuario.short_description = 'Usuário'  

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('n_projeto', 'titulo_projeto', 'status_projeto')

class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('projeto_titulo', 'valor_solicitado', 'n_parcelas', 'n_parcelas_pagas', 'status_pagamento', 'descricao')

    def projeto_titulo(self, obj):
        return obj.n_projeto.titulo_projeto
    projeto_titulo.short_description = 'Título do Projeto'



admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(Operacao, OperacaoAdmin)