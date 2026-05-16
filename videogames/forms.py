from django import forms
from .models import Videogame

class VideogameForm(forms.ModelForm):
    class Meta:
        model = Videogame
        # Excluimos los campos de auditoría porque se llenan solos
        fields = ['title', 'company', 'genre', 'platform', 'release_year', 'description']
        
        # Inyectamos clases de CSS para que los formularios se vean prolijos
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'platform': forms.TextInput(attrs={'class': 'form-control'}),
            'release_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }