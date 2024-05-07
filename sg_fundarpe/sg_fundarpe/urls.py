from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('login/', include('login.urls')),
    path('unat/', include('home.urls.unat')),
    path('uaff/', include('home.urls.uaff')),
    path('seju/', include('home.urls.seju')),
    path('presi/', include('home.urls.presi')),
    path('dif/', include('home.urls.dif')),
    path('asju/', include('home.urls.asju')),
    path('asgo/', include('home.urls.asgo')),
    path('adm/', include('home.urls.adm')), 
]

    