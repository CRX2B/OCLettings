"""
Ce module définit le modèle de base de données pour l'application profiles.

Il contient le modèle Profile qui étend le modèle User standard de Django
pour inclure des informations supplémentaires spécifiques aux utilisateurs
de l'application.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Représente le profil d'un utilisateur.

    Ce modèle est lié au modèle User standard de Django via une relation OneToOne.

    Attributs:
        user (User): La référence à l'instance User associée (relation OneToOne).
        favorite_city (str): La ville favorite de l'utilisateur (max 64 caractères, facultatif).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Retourne une représentation textuelle du profil (le nom d'utilisateur associé).

        Returns:
            str: Le nom d'utilisateur de l'objet User lié.
        """
        return self.user.username

    class Meta:
        """Métadonnées pour le modèle Profile."""
        verbose_name_plural = 'Profiles'
