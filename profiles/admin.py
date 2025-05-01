"""
Ce module configure l'interface d'administration Django pour l'application profiles.

Il enregistre le modèle Profile pour qu'il soit gérable via l'interface d'administration.
"""
from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
