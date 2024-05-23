from django.urls import path
from home.views.pdf import GeneratePdf

urlpatterns = [
    # outras URLs
    path('relatorio/pdf/', GeneratePdf.as_view(), name='generate_pdf'),
]
