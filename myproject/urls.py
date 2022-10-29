from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('entrada.urls')),
    path('', include('saida.urls')),
    path('', include('dashboard.urls')),
]
