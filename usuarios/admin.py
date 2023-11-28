from django.contrib import admin
from .models import *

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("username", "email")

admin.site.register(Usuario, UsuarioAdmin)