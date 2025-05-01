from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileModelTest(TestCase):
    """Tests unitaires pour le modèle Profile."""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass123')
        cls.profile = Profile.objects.create(user=cls.user, favorite_city='Test City')

    def test_profile_str(self):
        """Teste la méthode __str__ du modèle Profile."""
        self.assertEqual(str(self.profile), self.user.username)
