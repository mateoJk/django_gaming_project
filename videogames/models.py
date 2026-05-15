from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class Videogame(models.Model):
    # Usamos ayuda visual para el admin y validación de integridad
    title = models.CharField("Título del Juego", max_length=200)
    genre = models.CharField("Género", max_length=100)
    platform = models.CharField("Plataforma", max_length=100)
    
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