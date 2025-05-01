from django.test import TestCase, Client
from django.urls import reverse
from lettings.models import Address, Letting


class LettingIntegrationTest(TestCase):
    """Tests d'intégration pour le parcours utilisateur de base dans lettings."""

    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            number=777,
            street="Integration Ave",
            city="Integville",
            state="IN",
            zip_code=98765,
            country_iso_code="INT"
        )
        cls.letting = Letting.objects.create(
            title="Integration Test Letting",
            address=cls.address
        )
        cls.client = Client()

    def test_view_letting_integration(self):
        """Teste la création et la visualisation d'une location."""
        letting_url = reverse('lettings:letting', kwargs={'letting_id': self.letting.id})
        response = self.client.get(letting_url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'lettings/letting.html')

        self.assertContains(response, self.letting.title)
        self.assertContains(response, self.address.street)
        self.assertContains(response, self.address.city)

    def test_view_letting_list_integration(self):
        """Teste si la location créée apparaît dans la liste des locations."""
        index_url = reverse('lettings:index')
        response = self.client.get(index_url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'lettings/index.html')

        self.assertContains(response, self.letting.title)
