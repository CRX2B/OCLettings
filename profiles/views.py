"""
Ce module contient les vues pour l'application profiles.

Il définit les fonctions vues pour afficher l'index des profils
et les détails d'un profil utilisateur spécifique.
"""
from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):
    """Affiche la liste de tous les profils utilisateurs.

    Args:
        request: L'objet HttpRequest.

    Returns:
        HttpResponse: La réponse HTTP rendant la page d'index des profils
                      avec la liste des profils dans le contexte.
    """
    profiles_list = Profile.objects.all()
    context = {
        'profiles_list': profiles_list,
    }
    return render(request, 'profiles/index.html', context)


def profile_detail(request, username):
    """Affiche les détails d'un profil utilisateur spécifique.

    Récupère un profil par le nom d'utilisateur associé ou renvoie une erreur 404
    si l'utilisateur ou le profil n'existe pas.

    Args:
        request: L'objet HttpRequest.
        username (str): Le nom d'utilisateur associé au profil à afficher.

    Returns:
        HttpResponse: La réponse HTTP rendant la page de détail du profil
                      avec les informations du profil dans le contexte.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {
        'profile': profile,
    }
    return render(request, 'profiles/profile.html', context)
