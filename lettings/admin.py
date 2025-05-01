"""
Ce module configure l'interface d'administration Django pour l'application lettings.

Il enregistre les modèles Letting et Address pour qu'ils soient gérables
via l'interface d'administration.
"""
from django.contrib import admin
from .models import Letting, Address

admin.site.register(Letting)
admin.site.register(Address)
