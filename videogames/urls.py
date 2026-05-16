from django.urls import path
from . import views

# Nota Senior: Como usamos Class-Based Views, debemos llamarlas con '.as_view()'
urlpatterns = [
    path('', views.VideogameListView.as_view(), name='videogame_list'),
    path('<int:pk>/', views.VideogameDetailView.as_view(), name='videogame_detail'),
    path('nuevo/', views.VideogameCreateView.as_view(), name='videogame_create'),
    path('<int:pk>/editar/', views.VideogameUpdateView.as_view(), name='videogame_update'),
    path('<int:pk>/eliminar/', views.VideogameDeleteView.as_view(), name='videogame_delete'),
]