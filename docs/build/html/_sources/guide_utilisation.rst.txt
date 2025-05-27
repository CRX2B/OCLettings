Guide d'Utilisation
===================

Ce guide décrit les principaux cas d'utilisation de l'application Orange County Lettings du point de vue d'un utilisateur final naviguant sur le site.

Navigation Générale
-------------------

L'application présente une interface simple permettant d'accéder aux principales sections via des liens de navigation généralement présents en en-tête ou sur la page d'accueil.

Cas d'Utilisation Principaux
----------------------------

### 1. Consulter la liste des locations

*   **Point d'entrée :** L'utilisateur clique sur un lien "Lettings" ou "Locations" (ou accède directement à l'URL `/lettings/`).
*   **Action :** Le système affiche une page listant toutes les locations enregistrées. Chaque location est généralement représentée par son titre et potentiellement une image ou un bref descriptif.
*   **Résultat Attendu :** L'utilisateur peut parcourir la liste des biens disponibles.

### 2. Consulter les détails d'une location spécifique

*   **Point d'entrée :** Depuis la liste des locations, l'utilisateur clique sur le titre ou un lien "Détails" associé à une location spécifique.
*   **Action :** Le système affiche une page dédiée à cette location.
*   **Résultat Attendu :** L'utilisateur voit toutes les informations détaillées de la location sélectionnée, telles que son titre complet, son adresse complète (numéro, rue, ville, état, code postal, pays), et toute autre information pertinente enregistrée pour ce bien.

### 3. Consulter la liste des profils utilisateurs

*   **Point d'entrée :** L'utilisateur clique sur un lien "Profiles" (ou accède directement à l'URL `/profiles/`).
*   **Action :** Le système affiche une page listant tous les profils utilisateurs enregistrés dans l'application. Chaque profil est généralement représenté par le nom d'utilisateur.
*   **Résultat Attendu :** L'utilisateur peut parcourir la liste des profils.

### 4. Consulter les détails d'un profil utilisateur spécifique

*   **Point d'entrée :** Depuis la liste des profils, l'utilisateur clique sur le nom d'un utilisateur.
*   **Action :** Le système affiche une page dédiée à ce profil utilisateur.
*   **Résultat Attendu :** L'utilisateur voit les informations détaillées du profil sélectionné, telles que le nom d'utilisateur et sa ville favorite (si renseignée).

### 5. Accéder à l'interface d'administration (Administrateurs uniquement)

*   **Point d'entrée :** Un utilisateur avec les droits d'administration accède à l'URL `/admin/`.
*   **Action :**
    1.  Le système présente un formulaire de connexion.
    2.  L'administrateur saisit ses identifiants.
    3.  Après une authentification réussie, le système affiche le tableau de bord de l'administration Django.
*   **Résultat Attendu :** L'administrateur peut gérer toutes les données de l'application : créer, modifier, supprimer des utilisateurs, des profils, des adresses et des locations.

Ce guide couvre les interactions de base avec l'application. D'autres fonctionnalités pourraient exister ou être ajoutées ultérieurement. 