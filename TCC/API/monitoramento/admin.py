from django.contrib import admin
from monitoramento.models import Usuario

class Usuarios(admin.ModelAdmin):
    list_display = ('id','nome', 'cpf', 'data_nascimento', 'doenca')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Usuario, Usuarios)