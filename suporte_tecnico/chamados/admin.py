from django.contrib import admin
from .models import Usuario, Chamado

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email']

@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'usuario', 'data_criacao']
    list_filter = ['usuario', 'data_criacao']
