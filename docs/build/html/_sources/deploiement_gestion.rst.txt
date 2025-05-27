Déploiement et Gestion de l'Application
=======================================

Cette section décrit les procédures pour le déploiement et la gestion continue de l'application Orange County Lettings.

Plateforme de Déploiement
-------------------------

L'application est conçue pour être déployée en utilisant **Docker** et est actuellement hébergée sur **Render**.

*   **Docker :** L'application est conteneurisée à l'aide d'un `Dockerfile` qui définit l'environnement d'exécution, copie le code de l'application, installe les dépendances et spécifie la commande pour démarrer le serveur Gunicorn.
*   **Render :** Cette plateforme Cloud est utilisée pour construire l'image Docker à partir du dépôt GitHub et pour exécuter le conteneur. Render gère également la mise à l'échelle, les certificats SSL et d'autres aspects de l'infrastructure.

Processus de Déploiement Initial et Mises à Jour
------------------------------------------------

Le déploiement et les mises à jour sont largement automatisés grâce à l'intégration entre GitHub et Render, en s'appuyant sur le pipeline CI/CD configuré avec GitHub Actions.

1.  **Déclenchement du déploiement :**
    *   Un `push` sur la branche `master` du dépôt GitHub déclenche le workflow GitHub Actions.
    *   Le workflow exécute les tests, l'analyse de code, puis construit et publie l'image Docker sur Docker Hub.
    *   Render est configuré pour surveiller les nouvelles images sur Docker Hub (ou directement le dépôt GitHub) et déploie automatiquement la dernière version de l'image.

2.  **Commandes exécutées pendant le déploiement (par Render via le Dockerfile ou des commandes de démarrage) :**
    *   `python manage.py collectstatic --noinput` : Collecte tous les fichiers statiques (CSS, JS, images) dans un répertoire unique pour être servis en production (généralement par WhiteNoise).
    *   `python manage.py migrate` : Applique les migrations de base de données pour s'assurer que le schéma de la base de données est à jour avec les modèles Django.
    *   `gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT` : Lance le serveur d'application WSGI Gunicorn, qui écoute sur le port fourni par Render.

Gestion des Variables d'Environnement
-------------------------------------

Les configurations sensibles ou spécifiques à l'environnement (comme `SECRET_KEY`, `SENTRY_DSN`, `DEBUG`, `ALLOWED_HOSTS`) sont gérées comme des **variables d'environnement** directement dans l'interface d'administration de Render pour le service concerné.

*   Elles ne sont **pas** stockées dans le code source (à l'exception des valeurs par défaut pour le développement local).
*   Render injecte ces variables dans l'environnement du conteneur au moment de l'exécution.

Mises à Jour de l'Application
-----------------------------

Pour mettre à jour l'application en production :

1.  Effectuez les modifications de code souhaitées sur une branche de développement.
2.  Testez les modifications localement.
3.  Fusionnez (mergez) la branche de développement dans la branche `master`.
4.  Poussez (push) la branche `master` sur GitHub.
5.  Le pipeline CI/CD s'exécute, et si tout réussit, Render déploie automatiquement la nouvelle version.

Surveillance et Logs
--------------------

*   **Sentry :** Les erreurs en production sont rapportées à Sentry, permettant un suivi et un diagnostic rapides.
*   **Render :** La plateforme Render fournit des outils pour visualiser les logs de l'application en temps réel, ce qui est utile pour le débogage et la surveillance du comportement de l'application. 