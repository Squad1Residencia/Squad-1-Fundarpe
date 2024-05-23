import io
import tempfile
import matplotlib.pyplot as plt
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.colors import Color, HexColor
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from django.views import View
from home.models import Projeto, Pagamento, Usuario
from datetime import datetime
import os
from django.conf import settings

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []

        # Adiciona o logo e o título
        logo_path = os.path.join(settings.BASE_DIR, 'home', 'static', 'images', 'logomarcafundarpe.png')
        elements.append(Image(logo_path, width=200, height=60))
        elements.append(Paragraph(f"Relatório ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})", getSampleStyleSheet()["Title"]))

        # Subtitulo Pagamentos
        style = getSampleStyleSheet()["Heading2"]
        elements.append(Paragraph("Pagamentos", style))

        # pega os dados
        projetos = Projeto.objects.all()
        pagamentos = Pagamento.objects.all()
        usuarios = Usuario.objects.all()

        # Cria o primeiro gráfico
        plt.figure(figsize=(6, 4))
        status_labels = ['Concluído', 'Em Andamento']
        status_counts = [
            pagamentos.filter(status_pagamento='Concluído').count(),
            pagamentos.filter(status_pagamento='Em Andamento').count()
        ]
        chart_colors = [(0.1, 0.2, 0.5, 0.8), (0.2, 0.5, 0.7, 0.8)]
        plt.bar(status_labels, status_counts, color=chart_colors)
        plt.title('Status dos Pagamentos')
        plt.xlabel('Status')
        plt.ylabel('Número de Pagamentos')
        for i, count in enumerate(status_counts):
            plt.text(i, count, str(count), ha='center', va='bottom')

        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_chart:
            plt.savefig(temp_chart.name)
            chart1_path = temp_chart.name
        plt.close()
        elements.append(Image(chart1_path, width=500, height=300))

        # Cria o segundo gráfico
        plt.figure(figsize=(6, 4))
        valor_pago = sum(pagamento.valor_solicitado / pagamento.n_parcelas * (pagamento.n_parcelas_pagas if pagamento.n_parcelas_pagas is not None else 0) for pagamento in pagamentos)
        valor_a_ser_pago = sum((pagamento.valor_solicitado - (pagamento.valor_solicitado / pagamento.n_parcelas * (pagamento.n_parcelas_pagas if pagamento.n_parcelas_pagas is not None else 0))) for pagamento in pagamentos)
        labels = ['Valor Pago', 'Valor Pendente']
        values = [valor_pago, valor_a_ser_pago]
        plt.bar(labels, values, color=chart_colors)
        plt.title('Valores Pagos e Pendentes')
        plt.xlabel('Status')
        plt.ylabel('Valores')
        for i, value in enumerate(values):
            plt.text(i, value, f"{value:.2f}", ha='center', va='bottom')

        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_chart:
            plt.savefig(temp_chart.name)
            chart2_path = temp_chart.name
        plt.close()
        elements.append(Image(chart2_path, width=500, height=300))

        # Tabela de Pagamentos
        data = [['Projeto', 'Valor', 'Parcelas Pagas', 'Parcelas Totais', 'Status']]
        for pagamento in pagamentos:
            data.append([
                pagamento.n_projeto.titulo_projeto,
                f"{pagamento.valor_solicitado:.2f}",
                pagamento.n_parcelas_pagas,
                pagamento.n_parcelas,
                pagamento.status_pagamento
            ])
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), HexColor('#004080')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f2f2f2')),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)

        # Subtitulo Projetos
        elements.append(Paragraph("Projetos", style))

        # Tabela de Projetos
        data = [['Número do Projeto', 'Título do Projeto', 'Status']]
        for projeto in projetos:
            data.append([
                str(projeto.n_projeto),
                projeto.titulo_projeto,
                projeto.status_projeto
            ])
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), HexColor('#004080')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f2f2f2')),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)

        # Subtitulo Usuários
        elements.append(Paragraph("Usuários", style))

        # Tabela de Usuários
        data = [['Usuário', 'Departamento', 'Última Operação', 'Quantidade de Operações']]
        for usuario in usuarios:
            ultima_operacao = usuario.operacao_set.latest('data_cadastro') if usuario.operacao_set.exists() else None
            data.append([
                usuario.username,
                usuario.departamento,
                ultima_operacao.nome_operacao if ultima_operacao else 'Nenhuma operação encontrada',
                usuario.operacao_set.count()
            ])
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), HexColor('#004080')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f2f2f2')),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)

        doc.build(elements)
        buffer.seek(0)

        os.remove(chart1_path)
        os.remove(chart2_path)

        return FileResponse(buffer, as_attachment=True, filename='relatorio_projetos.pdf')
