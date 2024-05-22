from django.contrib import admin
from django.urls import path
from home.views.adm import *

urlpatterns = [
       path('', homepage, name = 'adm'),
      

]       