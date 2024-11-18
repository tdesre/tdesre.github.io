from django.urls import path
from . import views

urlpatterns = [
    # URL avec un paramètre dynamique 'text'
    path('feuilles/', views.catalogue_feuilles, name='catalogue_feuilles'),
    path('search/<str:text>/', views.species_search_view, name='species_search'),
    path('', views.catalogue_home, name='catalogue_home'),  # Page Catalogue
    path('feuilles/quiz/', views.quiz_view, name='quiz'),  # Nouveau chemin pour le quiz
]