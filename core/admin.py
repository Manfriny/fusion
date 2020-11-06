from django.contrib import admin
from .models import Cargo, Servico, Funcionario

# Register your models here.
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['cargo', 'criado', 'modificado', 'ativo']


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'criado', 'modificado', 'ativo')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'criado', 'modificado', 'ativo')