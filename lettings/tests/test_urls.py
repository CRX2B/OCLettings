from django.test import TestCase
from django.urls import reverse, resolve
from lettings.models import Address, Letting
from lettings import views


class LettingsURLTest(TestCase):
    """Tests unitaires pour les URLs de l'application lettings."""

    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            number=789,
            street="Other Ave",
            city="Othertown",
            state="OT",
            zip_code=11223,
            country_iso_code="GBR"
        )
        cls.letting = Letting.objects.create(
            title="URL Test Letting",
            address=cls.address
        )

    def test_index_url_reverse_resolve(self):
        """Teste l'inversion et la résolution de l'URL de l'index."""
        url_path = reverse('lettings:index')
        self.assertEqual(url_path, '/lettings/')
        self.assertEqual(resolve(url_path).func, views.lettings_index)

    def test_letting_url_reverse_resolve(self):
        """Teste l'inversion et la résolution de l'URL d'une location."""
        letting_id_to_test = self.letting.id
        url_path = reverse('lettings:letting', kwargs={'letting_id': letting_id_to_test})
        self.assertEqual(url_path, f'/lettings/{letting_id_to_test}/')
        self.assertEqual(resolve(url_path).func, views.letting_detail)
