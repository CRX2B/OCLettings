from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from profiles.models import Profile
from profiles import views


class ProfileURLTest(TestCase):
    """Tests unitaires pour les URLs de l'application profiles."""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass123')
        Profile.objects.create(user=cls.user, favorite_city='Test City')

    def test_index_url_reverse_resolve(self):
        """Teste l'inversion et la résolution de l'URL de l'index."""
        url_path = reverse('profiles:index')
        self.assertEqual(url_path, '/profiles/')
        self.assertEqual(resolve(url_path).func, views.profiles_index)

    def test_profile_url_reverse_resolve(self):
        """Teste l'inversion et la résolution de l'URL d'un profil."""
        username_to_test = self.user.username
        url_path = reverse('profiles:profile', kwargs={'username': username_to_test})
        self.assertEqual(url_path, f'/profiles/{username_to_test}/')
        self.assertEqual(resolve(url_path).func, views.profile_detail)
