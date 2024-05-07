from django.contrib import admin
from django.urls import path
from home.views.dif import *

urlpatterns = [
       path('', homepage, name = 'dif'),

]       