"""
Ce module contient les vues pour l'application lettings.

Il définit les fonctions vues pour afficher l'index des locations
et les détails d'une location spécifique.
"""
from django.shortcuts import render, get_object_or_404
from .models import Letting


def lettings_index(request):
    """Affiche la liste de toutes les locations disponibles.

    Args:
        request: L'objet HttpRequest.

    Returns:
        HttpResponse: La réponse HTTP rendant la page d'index des locations
                      avec la liste des locations dans le contexte.
    """
    lettings_list = Letting.objects.all()
    context = {
        'lettings_list': lettings_list,
    }
    return render(request, 'lettings/index.html', context)


def letting_detail(request, letting_id):
    """Affiche les détails d'une location spécifique.

    Récupère une location par son ID ou renvoie une erreur 404 si elle n'existe pas.

    Args:
        request: L'objet HttpRequest.
        letting_id (int): L'ID de la location à afficher.

    Returns:
        HttpResponse: La réponse HTTP rendant la page de détail de la location
                      avec les informations de la location dans le contexte.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
