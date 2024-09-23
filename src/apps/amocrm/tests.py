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

# The test cases above are for the ClientDataSerializer class.

# The test_valid_data method tests the serializer with valid data,
# and asserts that the serializer is valid and the validated data is equal to the input data.

# The test_invalid_data method tests the serializer with invalid data,
# and asserts that the serializer is not valid and the platform field is in the errors.

# The test_data_formatting method tests the formatting of the data by the serializer,
# and asserts that the data is equal to the input data.

# The test_empty_data method tests the serializer with empty data,
# and asserts that the serializer is not valid and all fields are in the errors.

# The test_invalid_phone_number method tests the serializer with an invalid phone number,
# and asserts that the serializer is not valid and the phone field is in the errors.

# These test cases cover various scenarios for the ClientDataSerializer class,
# ensuring that it behaves as expected in different situations.

# You can run the tests using the following command:
# python manage.py test src.amocrm.tests.TestClientDataSerializer
# This will run the test cases defined in the TestClientDataSerializer python manage.py test src.amocrm.test class.

# You can also run all tests in the amocrm app by running:
# python manage.py test src.amocrm
# This will run all test cases defined in the tests.py file of the amocrm app.