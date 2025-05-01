from django.test import TestCase, Client
from django.urls import reverse
from lettings.models import Address, Letting


class LettingViewTest(TestCase):
    """Tests unitaires pour les vues de l'application lettings."""

    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            number=101,
            street="View Test St",
            city="Viewville",
            state="VT",
            zip_code=54321,
            country_iso_code="XYZ"
        )
        cls.letting = Letting.objects.create(
            title="View Test Letting",
            address=cls.address
        )
        cls.client = Client()

    def test_lettings_index_view(self):
        """Teste la vue index des locations (statut, template)."""
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_letting_detail_view(self):
        """Teste la vue de détail d'une location (statut, template)."""
        url = reverse('lettings:letting', kwargs={'letting_id': self.letting.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')

    def test_letting_detail_view_not_found(self):
        """Teste la vue de détail pour une location inexistante (statut 404)."""
        url = reverse('lettings:letting', kwargs={'letting_id': 9999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
