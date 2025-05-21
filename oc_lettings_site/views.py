"""
Ce module contient les vues principales pour le projet oc_lettings_site.

Il définit la vue pour la page d'accueil ainsi que les gestionnaires
pour les erreurs 404 (Page non trouvée) et 500 (Erreur interne du serveur).
"""
import logging
from django.shortcuts import render


logger = logging.getLogger(__name__)


def index(request):
    """Affiche la page d'accueil du site.

    Args:
        request: L'objet HttpRequest.

    Returns:
        HttpResponse: La réponse HTTP rendant le template 'index.html'.
    """
    logger.info("Accès à la page d'accueil.")
    return render(request, 'index.html')


def custom_404(request, exception):
    """Gestionnaire personnalisé pour l'erreur 404 (Page non trouvée).

    Affiche une page d'erreur 404 personnalisée.

    Args:
        request: L'objet HttpRequest.
        exception: L'exception qui a déclenché l'erreur 404 (non utilisée ici).

    Returns:
        HttpResponse: La réponse HTTP rendant le template '404.html' avec un statut 404.
    """
    logger.error(f"Erreur 404 déclenchée pour le chemin: {request.path}", exc_info=True)
    return render(request, "404.html", status=404)


def custom_500(request):
    """Gestionnaire personnalisé pour l'erreur 500 (Erreur interne du serveur).

    Affiche une page d'erreur 500 personnalisée.

    Args:
        request: L'objet HttpRequest.

    Returns:
        HttpResponse: La réponse HTTP rendant le template '500.html' avec un statut 500.
    """
    logger.error("Erreur interne du serveur (500) déclenchée.", exc_info=True)
    return render(request, "500.html", status=500)
