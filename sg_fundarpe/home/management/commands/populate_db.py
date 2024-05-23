from django.core.management.base import BaseCommand
from django.utils import timezone
from home.models import Projeto, Operacao, Pagamento, Usuario
import random

class Command(BaseCommand):
    help = 'Popula o banco de dados com projetos artísticos'

    def handle(self, *args, **kwargs):
        # Lista de nomes de projetos artísticos
        nomes_projetos_artistico = [
            'Arte Urbana',
            'Pintura Contemporânea',
            'Escultura Moderna',
            'Teatro Experimental',
            'Dança Contemporânea',
            'Cinema Independente',
            'Fotografia Artística',
            'Música Instrumental',
            'Performance Artística',
            'Instalação Interativa',
            'Literatura Fantástica',
            'Poesia Visual',
            'Videoclipes Criativos',
            'Arte Digital',
            'Cerâmica Artística',
            'Grafite e Murais',
            'Quadrinhos e Ilustração',
            'Design de Moda',
            'Animação Stop Motion',
            'Documentário Cultural',
            'Artivismo',
            'Arte Ambiental',
            'Arquitetura Efêmera',
            'Arte Têxtil',
            'Narrativas Visuais',
            'Arte e Tecnologia',
            'Arte Sonora',
            'Projetos Multimídia',
            'Arte Pública',
            'Arte Inclusiva'
        ]

        # Valores e parcelas para os projetos
        valores_solicitados = [random.randint(1000, 10000) for _ in range(30)]
        parcelas = [random.randint(1, 10) for _ in range(30)]
        parcelas_pagas = [random.randint(0, n_parcelas) for n_parcelas in parcelas]  # Definindo parcelas pagas aleatórias

        # Buscar o usuário 'unat' no banco de dados
        try:
            usuario = Usuario.objects.get(username='unat')
        except Usuario.DoesNotExist:
            self.stdout.write(self.style.ERROR("Usuário 'unat' não encontrado"))
            return

        for i in range(30):
            n_projeto =+ i  
            titulo_projeto = nomes_projetos_artistico[i]
            n_sei = str(n_projeto)  # Agora `n_sei` é uma string
            valor_solicitado = valores_solicitados[i]
            n_parcelas = parcelas[i]
            n_parcelas_pagas = parcelas_pagas[i]
            status_pagamento = 'Concluído' if n_parcelas_pagas == n_parcelas else 'Em andamento'

            projeto, created = Projeto.objects.get_or_create(
                n_projeto=n_projeto,
                defaults={'titulo_projeto': titulo_projeto, 'n_sei': n_sei, 'status_projeto': '1'},
            )

            if not created:
                projeto.titulo_projeto = titulo_projeto
                projeto.n_sei = n_sei
                projeto.status_projeto = '1'
                projeto.save()

            operacao = Operacao()
            operacao.n_projeto = projeto
            operacao.id_usuario = usuario
            operacao.status_operacao = 'Editado' if not created else 'Criado'
            operacao.nome_operacao = 'Projeto Editado' if not created else 'Projeto Criado'
            operacao.data_operacao = timezone.now()
            operacao.save()

            novo_pagamento, created = Pagamento.objects.get_or_create(
                n_projeto=projeto,
                defaults={
                    'valor_solicitado': valor_solicitado,
                    'n_parcelas': n_parcelas,
                    'n_parcelas_pagas': n_parcelas_pagas,
                    'status_pagamento': status_pagamento
                },
            )

            if not created:
                novo_pagamento.valor_solicitado = valor_solicitado
                novo_pagamento.n_parcelas = n_parcelas
                novo_pagamento.n_parcelas_pagas = n_parcelas_pagas
                novo_pagamento.status_pagamento = status_pagamento
                novo_pagamento.save()

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso!"))
