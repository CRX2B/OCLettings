# Orange County Lettings

Site web de location immobilière pour Orange County.

## Documentation Complète

Pour une documentation détaillée du projet, incluant l'architecture, le guide d'installation, les technologies utilisées, et plus encore, veuillez consulter notre documentation sur Read the Docs :
[**Documentation Orange County Lettings sur Read the Docs**](https://oclettings-13.readthedocs.io/fr/latest/)

## Aperçu

Le site web permet de consulter des locations (`lettings`) et des profils d'utilisateurs (`profiles`). Il est construit avec Django et utilise une base de données SQLite pour le développement.

## Développement Local

### Prérequis

*   Git CLI
*   Python (version 3.9 ou supérieure recommandée, vérifiez `runtime.txt` ou la configuration de déploiement pour la version exacte utilisée en production)
*   SQLite3 CLI (optionnel, pour inspecter la base de données directement)

### Instructions d'Installation et de Lancement

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/CRX2B/OCLettings
    cd Python-OC-Lettings-FR
    ```

2.  **Créer et activer un environnement virtuel :**
    *   Sur macOS / Linux :
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   Sur Windows (PowerShell) :
        ```bash
        python -m venv venv
        .\venv\Scripts\Activate.ps1
        ```

3.  **Installer les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Appliquer les migrations (si nécessaire) :**
    ```bash
    python manage.py migrate
    ```

5.  **Lancer le serveur de développement :**
    ```bash
    python manage.py runserver
    ```
    Le site sera accessible à l'adresse `http://localhost:8000`.

### Outils de Qualité

*   **Linting (avec Flake8) :**
    ```bash
    flake8 .
    ```
*   **Tests Unitaires (avec Pytest) :**
    ```bash
    pytest
    ```
    Pour voir la couverture de code :
    ```bash
    pytest --cov=.
    ```

### Base de Données

Le projet utilise SQLite en développement (`oc-lettings-site.sqlite3`). Vous pouvez l'inspecter avec des outils comme `sqlite3` ou DB Browser for SQLite.

### Panel d'Administration Django

*   Accessible via `/admin/` sur le serveur de développement.
*   Créez un superutilisateur si vous n'en avez pas :
    ```bash
    python manage.py createsuperuser
    ```

## Déploiement

Le déploiement est géré via une pipeline CI/CD avec GitHub Actions, qui construit une image Docker et la déploie sur Render.com. Consultez le fichier `.github/workflows/ci_cd.yml` pour plus de détails.

## Configuration CI/CD (GitHub Actions Secrets)

Pour que le pipeline CI/CD défini dans `.github/workflows/ci_cd.yml` fonctionne correctement, les secrets suivants doivent être configurés dans les "Secrets and variables" > "Actions" de votre dépôt GitHub :

*   `SECRET_KEY`: Clé secrète Django. Vous pouvez en générer une nouvelle (par exemple avec `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`).
*   `SENTRY_DSN`: (Optionnel) Le DSN de votre projet Sentry pour le suivi des erreurs. Si vous n'utilisez pas Sentry, vous pouvez mettre une valeur vide ou omettre certaines configurations liées dans le workflow.
*   `DOCKERHUB_USERNAME`: Votre nom d'utilisateur Docker Hub, utilisé pour pousser l'image Docker.
*   `DOCKERHUB_TOKEN`: Un token d'accès Docker Hub avec les permissions nécessaires pour pousser des images. Il est recommandé d'utiliser un token plutôt que votre mot de passe direct.
*   `RENDER_WEBHOOK`: L'URL du "Deploy Hook" fournie par Render pour votre service, utilisée pour déclencher les redéploiements.

