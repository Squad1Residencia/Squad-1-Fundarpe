from django.contrib import admin
from django.urls import path
from home.views.uaff import *

urlpatterns = [
       path('', homepage, name = 'uaff'),
       path('cadastro_uaff/', cadastro_uaff , name='cadastro_uaff'),
       path('cadastro_uaff1/', cadastro_uaff1 , name='cadastro_uaff1'),

]       