"""
Ce module définit les modèles de base de données pour l'application lettings.

Il contient les modèles Address et Letting pour stocker les informations
sur les adresses et les locations correspondantes.
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Représente une adresse postale complète.

    Attributs:
        number (int): Le numéro de la rue (max 9999).
        street (str): Le nom de la rue (max 64 caractères).
        city (str): Le nom de la ville (max 64 caractères).
        state (str): L'état ou la province (exactement 2 caractères).
        zip_code (int): Le code postal (max 99999).
        country_iso_code (str): Le code ISO du pays (exactement 3 caractères).
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """Retourne une représentation textuelle de l'adresse (numéro et rue).

        Returns:
            str: Le numéro suivi du nom de la rue.
        """
        return f'{self.number} {self.street}'

    class Meta:
        """Métadonnées pour le modèle Address."""
        verbose_name_plural = 'Addresses'


class Letting(models.Model):
    """Représente une location associée à une adresse.

    Attributs:
        title (str): Le titre de la location (max 256 caractères).
        address (Address): La référence à l'adresse de la location (relation OneToOne).
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Retourne une représentation textuelle de la location (son titre).

        Returns:
            str: Le titre de la location.
        """
        return self.title

    class Meta:
        """Métadonnées pour le modèle Letting."""
        verbose_name_plural = 'Lettings'
