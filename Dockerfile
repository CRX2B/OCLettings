# Image de base Python légère
FROM python:3.12-slim

# Variables d'environnement Python optimisées
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copie et installation des dépendances Python
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copie des sources de l'application
COPY . .

# Création d'un utilisateur et groupe non-root 'django'
RUN groupadd -r django && \
    useradd --no-create-home -r -g django django

# Création du répertoire pour les statiques et attribution des permissions à /app
RUN mkdir -p /app/staticfiles && \
    chown -R django:django /app

# Passage à l'utilisateur non-root 'django'
USER django

# Port exposé par l'application
EXPOSE 8000

# Collecte des fichiers statiques de Django
RUN python manage.py collectstatic --noinput --clear

# Commande de démarrage de l'application avec Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]