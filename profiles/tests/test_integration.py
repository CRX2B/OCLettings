from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileIntegrationTest(TestCase):
    """Tests d'intégration pour le parcours utilisateur de base dans profiles."""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='integ_user', password='integ_pass123')
        cls.profile = Profile.objects.create(user=cls.user, favorite_city='Integ City')
        cls.client = Client()

    def test_view_profile_integration(self):
        """Teste la création et la visualisation d'un profil."""
        profile_url = reverse('profiles:profile', kwargs={'username': self.user.username})
        response = self.client.get(profile_url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'profiles/profile.html')

        self.assertContains(response, self.user.username)
        self.assertContains(response, self.profile.favorite_city)

    def test_view_profile_list_integration(self):
        """Teste si le profil créé apparaît dans la liste des profils."""
        index_url = reverse('profiles:index')
        response = self.client.get(index_url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'profiles/index.html')

        self.assertContains(response, self.user.username)
