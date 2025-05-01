from django.test import TestCase
from django.urls import reverse, resolve
from oc_lettings_site import views


class ProjectURLTest(TestCase):
    """Tests unitaires pour les URLs globales du projet."""

    def test_index_url_reverse_resolve(self):
        """Teste l'inversion et la résolution de l'URL racine."""
        url_path = reverse('index')
        self.assertEqual(url_path, '/')
        self.assertEqual(resolve(url_path).func, views.index)

    def test_admin_url_reverse_resolve(self):
        """Teste l'inversion et la résolution de l'URL de l'admin."""
        url_path = reverse('admin:index')
        self.assertEqual(url_path, '/admin/')
        self.assertEqual(resolve(url_path).namespace, 'admin')

    def test_lettings_include_resolves(self):
        """Vérifie que /lettings/ pointe vers le bon namespace."""
        url_path_within_app = reverse('lettings:index')
        self.assertEqual(url_path_within_app, '/lettings/')
        self.assertEqual(resolve(url_path_within_app).namespace, 'lettings')

    def test_profiles_include_resolves(self):
        """Vérifie que /profiles/ pointe vers le bon namespace."""
        url_path_within_app = reverse('profiles:index')
        self.assertEqual(url_path_within_app, '/profiles/')
        self.assertEqual(resolve(url_path_within_app).namespace, 'profiles')
