from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Projeto, Pagamento, Operacao

class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'departamento', 'precisa_redefinir_senha']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('departamento', 'precisa_redefinir_senha')}),
    )

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Projeto)
admin.site.register(Pagamento)
admin.site.register(Operacao)