from django.urls import path
from . import views  # Importa as views do aplicativo login

urlpatterns = [
    path('', views.login_view, name='login'),  
    
]