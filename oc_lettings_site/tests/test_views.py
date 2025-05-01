from django.test import TestCase, Client
from django.urls import reverse


class ProjectViewTest(TestCase):
    """Tests unitaires pour les vues globales du projet."""

    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        """Teste la vue de la page d'accueil (statut, template)."""
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_admin_view_loads(self):
        """Teste que la page de login de l'admin se charge."""
        url = reverse('admin:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/admin/login/'))

        login_url = response.url
        login_response = self.client.get(login_url)
        self.assertEqual(login_response.status_code, 200)
        self.assertTemplateUsed(login_response, 'admin/login.html')
