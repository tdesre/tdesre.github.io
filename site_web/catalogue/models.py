from django.db import models
from django.contrib.auth.models import User  # Utilisé pour associer les notes aux utilisateurs

class Species(models.Model):
    name = models.CharField(max_length=200, unique=True)
    name_leaf = models.CharField(max_length=200, unique=True, blank=True)
    name_fruit = models.CharField(max_length=200, unique=True, blank=True)
    file_leaf = models.CharField(max_length=200, unique=True, blank=True)
    file_fruit = models.CharField(max_length=200, unique=True, blank=True)
    description = models.CharField(max_length=100000, unique=True, blank=True)
    folder_gallery = models.CharField(max_length=200, unique=True, blank=True)
    keywords = models.CharField(max_length=1000, unique=False, blank=True)
    

def __str__(self):
    return self.name

