Structure de la Base de Données et Modèles
===========================================

L'application Orange County Lettings utilise une base de données relationnelle pour stocker les informations sur les locations et les profils utilisateurs.

Système de Gestion de Base de Données (SGBD)
--------------------------------------------

Par défaut, et pour la simplicité du développement et du déploiement initial, le projet est configuré pour utiliser **SQLite**. Les données sont stockées dans un fichier `oc-lettings-site.sqlite3` à la racine du projet.

Modèles de Données (ORM Django)
-------------------------------

L'interaction avec la base de données est gérée via l'ORM (Object-Relational Mapper) de Django. Les modèles définissent la structure des tables de la base de données et fournissent une interface Python pour interroger et manipuler les données.

Le projet est structuré en deux applications Django principales, chacune avec ses propres modèles :

### Modèles de l'application `lettings`

L'application `lettings` gère les informations relatives aux biens immobiliers proposés à la location.

**Modèle `Address`**

.. code-block:: python


   from django.db import models
   from django.core.validators import MaxValueValidator, MinLengthValidator

   class Address(models.Model):
       number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
       street = models.CharField(max_length=64)
       city = models.CharField(max_length=64)
       state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
       zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
       country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

       def __str__(self):
           return f'{self.number} {self.street}'

       class Meta:
           verbose_name_plural = "Addresses"

*   **Rôle :** Représente une adresse postale complète.
*   **Champs :**
    *   `number`: Numéro dans la rue (entier positif, max 9999).
    *   `street`: Nom de la rue (chaîne, max 64 caractères).
    *   `city`: Ville (chaîne, max 64 caractères).
    *   `state`: État/Province (chaîne, 2 caractères).
    *   `zip_code`: Code postal (entier positif, max 99999).
    *   `country_iso_code`: Code ISO du pays (chaîne, 3 caractères).
*   **Méthode `__str__` :** Retourne le numéro et le nom de la rue.
*   **Meta :**
    *   `verbose_name_plural`: Définit le nom pluriel du modèle utilisé dans l'interface d'administration Django comme "Addresses".

**Modèle `Letting`**

.. code-block:: python


   class Letting(models.Model):
       title = models.CharField(max_length=256)
       address = models.OneToOneField(Address, on_delete=models.CASCADE)

       def __str__(self):
           return self.title

       class Meta:
           verbose_name_plural = "Lettings"

*   **Rôle :** Représente une location et est associé à une instance du modèle `Address`.
*   **Champs :**
    *   `title`: Titre de l'annonce de location (chaîne, max 256 caractères).
    *   `address`: Lien vers une instance du modèle `Address` (relation un-à-un). La suppression de l'adresse entraîne la suppression de la location.
*   **Méthode `__str__` :** Retourne le titre de la location.
*   **Meta :**
    *   `verbose_name_plural`: Définit le nom pluriel du modèle utilisé dans l'interface d'administration Django comme "Lettings".

### Modèles de l'application `profiles`

L'application `profiles` gère les informations des profils utilisateurs.

**Modèle `Profile`**

.. code-block:: python


   from django.db import models
   from django.contrib.auth.models import User

   class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       favorite_city = models.CharField(max_length=64, blank=True)

       def __str__(self):
           return self.user.username

       class Meta:
           verbose_name_plural = "Profiles"

*   **Rôle :** Étend le modèle `User` standard de Django pour ajouter des informations spécifiques au profil.
*   **Champs :**
    *   `user`: Lien vers une instance du modèle `User` de Django (relation un-à-un). La suppression de l'utilisateur entraîne la suppression du profil.
    *   `favorite_city`: Ville favorite de l'utilisateur (chaîne, max 64 caractères, champ optionnel).
*   **Méthode `__str__` :** Retourne le nom d'utilisateur associé au profil.
*   **Meta :**
    *   `verbose_name_plural`: Définit le nom pluriel du modèle utilisé dans l'interface d'administration Django comme "Profiles". 