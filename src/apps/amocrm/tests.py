from django.core.serializers import serialize
from django.test import TestCase

from .serializers import ClientDataSerializer

# unit tests for your views and serializers independently.
# Testing serializers for validation and data formatting is a good practice.

class TestClientDataSerializer(TestCase):
    def test_valid_data(self):
        data = {
            "name": "John Doe",
            "phone": "+998993233528",
            "service": "Service",
            "platform": "Platform"
        }
        serializer = ClientDataSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, data)

    def test_invalid_data(self):
        data = {
                "name": "John Doe",
                "phone": "+998993233528",
                "service": "Service",
        }
        serializer = ClientDataSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("platform", serializer.errors)

    def test_data_formatting(self):
        data = {
            "name": "John Doe",
            "phone": "+998993233528",
            "service": "Service",
            "platform": "Platform"
        }
        serializer = ClientDataSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.data, data)

        formatted_data = {
            "name": "John Doe",
            "phone": "+998993233528",
            "service": "Service",
            "platform": "Platform"
        }
        self.assertEqual(serializer.data, formatted_data)

    def test_empty_data(self):
        data = {}
        serializer = ClientDataSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)
        self.assertIn("phone", serializer.errors)
        self.assertIn("service", serializer.errors)
        self.assertIn("platform", serializer.errors)

    def test_invalid_phone_number(self):
        data = {
            "name": "John Doe",
            "phone": "1234567890",
            "service": "Service",
            "platform": "Platform"
        }
        serializer = ClientDataSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("phone", serializer.errors)