from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileViewTest(TestCase):
    """Tests unitaires pour les vues de l'application profiles."""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass123')
        cls.profile = Profile.objects.create(user=cls.user, favorite_city='Test City')
        cls.client = Client()

    def test_profiles_index_view(self):
        """Teste la vue index des profils (statut, template)."""
        url = reverse('profiles:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_profile_detail_view(self):
        """Teste la vue de détail d'un profil (statut, template)."""
        url = reverse('profiles:profile', kwargs={'username': self.user.username})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_detail_view_not_found(self):
        """Teste la vue de détail pour un profil inexistant (statut 404)."""
        url = reverse('profiles:profile', kwargs={'username': 'nonexistentuser'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
