from django.urls import path
from . import views  

urlpatterns = [
    path('', views.login_view, name='login'),
    path('redefinir_senha/', views.redefinir_senha_view, name='redefinir_senha'),
    
]