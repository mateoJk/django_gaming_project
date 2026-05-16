from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Videogame
from .forms import VideogameForm

# 1. READ (Lista de Videojuegos) - Ya la tenías, ahora la optimizamos a CBV
class VideogameListView(ListView):
    model = Videogame
    template_name = 'videogames/list.html'
    context_object_name = 'videogames'

# 2. READ (Detalle de un Videojuego específico)
class VideogameDetailView(DetailView):
    model = Videogame
    template_name = 'videogames/detail.html'
    context_object_name = 'game'

# 3. CREATE (Formulario para añadir juego)
class VideogameCreateView(CreateView):
    model = Videogame
    form_class = VideogameForm
    template_name = 'videogames/form.html'
    # Redirige al catálogo de juegos cuando se crea con éxito
    success_url = reverse_lazy('videogame_list')

# 4. UPDATE (Formulario para editar juego)
class VideogameUpdateView(UpdateView):
    model = Videogame
    form_class = VideogameForm
    template_name = 'videogames/form.html' # Reutilizamos el mismo template del formulario
    success_url = reverse_lazy('videogame_list')

# 5. DELETE (Confirmación para borrar juego)
class VideogameDeleteView(DeleteView):
    model = Videogame
    template_name = 'videogames/confirm_delete.html'
    success_url = reverse_lazy('videogame_list')