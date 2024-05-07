from django.contrib import admin
from django.urls import path
from home.views.presi import *

urlpatterns = [
       path('', homepage, name = 'presi'),

]       