from django.urls import path
from . import views

urlpatterns = [
    path('feuilles/', views.catalogue_feuilles, name='catalogue_feuilles'), # pour accéder au catalogue des feuilles
    path('fruits/', views.catalogue_fruits, name='catalogue_fruits'), # pour accéder au catalogue des fruits
    path('feuilles/quiz/', views.quiz_view, name='quiz'),  # pour acceder au quizz
    path('feuilles/<str:species_name>/', views.species_detail, name='species_detail'),  
    path('search/<str:text>/', views.species_search_view, name='species_search'), 
    path('description/<int:id>/', views.species_detail, name='species_detail_view'),
]
