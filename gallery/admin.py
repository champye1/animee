from django.contrib import admin
from .models import Galeria, Comentario

class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 0

@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('title', 'linea', 'tipo', 'description')
    list_filter = ('linea', 'tipo')
    search_fields = ('title', 'description')
    list_per_page = 10
    ordering = ('title',)
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('title', 'description', 'imagen')
        }),
        ('Clasificación', {
            'fields': ('linea', 'tipo'),
            'classes': ('collapse',)
        }),
    )
    
    list_editable = ('linea', 'tipo')
    
    inlines = [ComentarioInline]

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'galeria', 'texto', 'fecha')
    list_filter = ('galeria__tipo', 'galeria__linea', 'usuario', 'fecha')
    search_fields = ('texto', 'usuario__username', 'galeria__title')
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)


