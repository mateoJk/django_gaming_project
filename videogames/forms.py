from django import forms
from .models import Videogame

class VideogameForm(forms.ModelForm):
    class Meta:
        model = Videogame
        fields = ['title', 'company', 'genre', 'platform', 'release_year', 'description','image']
        
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'image': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 mt-1 bg-gray-50 border border-gray-300 rounded-md text-gray-900 focus:ring-blue-500 focus:border-blue-500 block sm:text-sm shadow-sm'
            })