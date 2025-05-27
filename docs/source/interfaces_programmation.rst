Interfaces de Programmation
===========================

Bien que l'application Orange County Lettings ne dispose pas d'une API REST publique distincte, ses fonctionnalités sont accessibles via un ensemble d'URLs (routes) gérées par Django. Chaque URL est associée à une vue qui traite la requête et renvoie une réponse HTML.

Voici les principales interfaces (URLs et vues) de l'application :

Page d'Accueil
--------------

*   **URL :** `/`
*   **Vue :** `oc_lettings_site.views.index`
*   **Description :** Affiche la page d'accueil principale de l'application.

Application Lettings (Locations)
--------------------------------

Gère l'affichage des locations.

*   **Liste des locations :**
    *   **URL :** `/lettings/`
    *   **Vue :** `lettings.views.index`
    *   **Description :** Affiche une liste de toutes les locations disponibles.

*   **Détail d'une location :**
    *   **URL :** `/lettings/<int:letting_id>/`
    *   **Vue :** `lettings.views.letting`
    *   **Description :** Affiche les informations détaillées pour une location spécifique, identifiée par son `letting_id`.

Application Profiles (Profils)
------------------------------

Gère l'affichage des profils utilisateurs.

*   **Liste des profils :**
    *   **URL :** `/profiles/`
    *   **Vue :** `profiles.views.index`
    *   **Description :** Affiche une liste de tous les profils utilisateurs enregistrés.

*   **Détail d'un profil :**
    *   **URL :** `/profiles/<str:username>/`
    *   **Vue :** `profiles.views.profile`
    *   **Description :** Affiche les informations détaillées pour un profil utilisateur spécifique, identifié par son `username`.

Interface d'Administration Django
---------------------------------

*   **URL :** `/admin/`
*   **Description :** Fournit une interface web complète pour la gestion des données de l'application (utilisateurs, profils, adresses, locations). L'accès est réservé aux superutilisateurs.

Ces URLs constituent les principaux points d'entrée pour interagir avec l'application via un navigateur web. 