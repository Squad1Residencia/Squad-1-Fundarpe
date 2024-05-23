from django.core.management.base import BaseCommand
from home.models import Projeto, Operacao, Pagamento

class Command(BaseCommand):
    help = 'Limpa o banco de dados de Projetos, Operacoes e Pagamentos'

    def handle(self, *args, **options):
        # Remover todos os Projetos, Operacoes e Pagamentos
        Projeto.objects.all().delete()
        Operacao.objects.all().delete()
        Pagamento.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("As tabelas  foram limpas!"))