from django.test import TestCase
from lettings.models import Address, Letting
from django.core.exceptions import ValidationError


class AddressModelTest(TestCase):
    """Tests unitaires pour le modèle Address."""

    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="USA"
        )

    def test_address_str(self):
        """Teste la méthode __str__ du modèle Address."""
        self.assertEqual(str(self.address), "123 Test Street")

    def test_address_validators(self):
        """Teste les validateurs du modèle Address."""
        with self.assertRaises(ValidationError):
            address_invalid_state = Address(
                number=1, street="S", city="C", state="T", zip_code=1, country_iso_code="COU"
            )
            address_invalid_state.full_clean()
        with self.assertRaises(ValidationError):
            address_invalid_iso = Address(
                number=1, street="S", city="C", state="TS", zip_code=1, country_iso_code="CO"
            )
            address_invalid_iso.full_clean()
        with self.assertRaises(ValidationError):
            address_invalid_zip = Address(
                number=1, street="S", city="C", state="TS", zip_code=100000, country_iso_code="COU"
            )
            address_invalid_zip.full_clean()


class LettingModelTest(TestCase):
    """Tests unitaires pour le modèle Letting."""

    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            number=456,
            street="Main St",
            city="Anytown",
            state="AN",
            zip_code=67890,
            country_iso_code="CAN"
        )
        cls.letting = Letting.objects.create(
            title="Test Letting Title",
            address=cls.address
        )

    def test_letting_str(self):
        """Teste la méthode __str__ du modèle Letting."""
        self.assertEqual(str(self.letting), "Test Letting Title")
