from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date


class Company(models.Model):
    name = models.CharField("Nombre de la Compañía", max_length=150, unique=True)
    country = models.CharField("País de Origen", max_length=100, blank=True)
    website = models.URLField("Sitio Web", blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Compañía"
        verbose_name_plural = "Compañías"
        ordering = ['name']

    def __str__(self):
        return self.name

class Videogame(models.Model):
    # Usamos ayuda visual para el admin y validación de integridad
    title = models.CharField("Título del Juego", max_length=200)
    genre = models.CharField("Género", max_length=100)
    platform = models.CharField("Plataforma", max_length=100)

    # Establecemos la relación de clave foránea. 
    # 'on_delete=models.CASCADE' significa que si se borra una compañía, se borrarán automáticamente todos sus videojuegos asociados.
    # 'related_name' nos permite hacer consultas inversas (ej: company.games.all())
    company = models.ForeignKey(
        Company, 
        on_delete=models.CASCADE, 
        related_name="games", 
        verbose_name="Desarrolladora",
        null=True, # Lo dejamos temporalmente null para que la base de datos no joda con datos viejos
        blank=False
    )
    
    # valida los rangos de números
    release_year = models.IntegerField(
        "Año de Lanzamiento",
        validators=[
            MinValueValidator(1950), 
            MaxValueValidator(date.today().year + 5)
        ]
    )
    
    description = models.TextField("Descripción", blank=True, help_text="Breve resumen del juego")
    
    # Campos de auditoría 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Videojuego"
        verbose_name_plural = "Videojuegos"
        ordering = ['-release_year'] # Los más nuevos aparecen primero

    def __str__(self):
        return f"{self.title} ({self.release_year})"