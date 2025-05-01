from django.test import TestCase, Client
from django.urls import reverse


class ProjectIntegrationTest(TestCase):
    """Tests d'intégration pour la navigation de base du projet."""

    def setUp(self):
        self.client = Client()

    def test_navigation_from_home(self):
        """Teste la navigation de la page d'accueil vers les index des apps."""
        home_url = reverse('index')
        response = self.client.get(home_url)
        self.assertEqual(response.status_code, 200)

        lettings_index_url = reverse('lettings:index')
        profiles_index_url = reverse('profiles:index')

        self.assertContains(response, f'href="{lettings_index_url}"')
        self.assertContains(response, f'href="{profiles_index_url}"')

        lettings_response = self.client.get(lettings_index_url)
        self.assertEqual(lettings_response.status_code, 200)
        self.assertTemplateUsed(lettings_response, 'lettings/index.html')

        profiles_response = self.client.get(profiles_index_url)
        self.assertEqual(profiles_response.status_code, 200)
        self.assertTemplateUsed(profiles_response, 'profiles/index.html')
