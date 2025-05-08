from django.contrib import admin
from .models import Scheduling

@admin.register(Scheduling)
class SchedulingAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'date', 'time', 'specialty')
    list_filter = ('date', 'specialty')
    search_fields = ('name', 'cpf', 'specialty')
    ordering = ('-date', 'time')

    fieldsets = (
        (None, {
            'fields': ('name', 'cpf', 'date', 'time', 'specialty')
        }),
        ('Observações', {
            'classes': ('collapse',),
            'fields': ('observations',),
        }),
    )
