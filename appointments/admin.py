from django.contrib import admin
from .models import Scheduling

@admin.register(Scheduling)
class SchedulingAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'date', 'time', 'specialty')  # Colunas na lista
    list_filter = ('date', 'specialty')  # Filtros laterais
    search_fields = ('name', 'cpf', 'specialty')  # Campo de busca
    ordering = ('-date', 'time')  # Ordenação padrão

    fieldsets = (
        (None, {
            'fields': ('name', 'cpf', 'date', 'time', 'specialty')
        }),
        ('Observações', {
            'classes': ('collapse',),
            'fields': ('observations',),
        }),
    )
