from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('barbearia.urls')),
    path('auth/', include('usuarios.urls')),
    path('', include('agenda.urls')),
    path('admin/', admin.site.urls),
]