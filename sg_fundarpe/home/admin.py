from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Projeto)
admin.site.register(Usuario)
admin.site.register(Pagamento)
admin.site.register(Operacao)