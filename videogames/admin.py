from django.contrib import admin
from .models import Videogame, Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    # Columnas que se mostrarán en la lista
    list_display = ('name', 'country', 'website')
    # Barra de búsqueda integrada por nombre y país
    search_fields = ('name', 'country')


@admin.register(Videogame)
class VideogameAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'genre', 'platform', 'release_year')

    # list_filter añade un panel lateral derecho para filtrar con un clic
    list_filter = ('genre', 'platform', 'release_year', 'company')

    # search_fields permite buscar por texto libre
    search_fields = ('title', 'genre', 'description')

    autocomplete_fields = ['company']