from django.test import TestCase, Client
from .models import Patient
from .dataflow_pipeline import preprocess_ecg
import unittest


class TestPatientDashboardView(TestCase):

    def setUp(self):
        # Create a test patient
        self.patient = Patient.objects.create(name="Test Patient", date_of_birth="1990-01-01")
        self.client = Client()

    def test_view_returns_200(self):
        response = self.client.get(f'/patient/{self.patient.pk}/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_view_context(self):
        response = self.client.get(f'/patient/{self.patient.pk}/dashboard/')
        self.assertIn('heart_rate', response.context)



class TestPreprocessing(unittest.TestCase):

    def test_normalization(self):
        # Creating sample ECG data
        ecg_data = [100, 120, 110, 90, 130]
        expected_output = [0.2, 0.6, 0.4, 0.0, 0.8]  # Assuming normalization is in range of 0-1

        # Calling the preprocess_ecg function
        processed_data = preprocess_ecg({'ecg_data': ecg_data})

        # Checking if the 'ecg_data' key exists and the values are as expected
        self.assertIn('ecg_data', processed_data)
        self.assertEqual(processed_data['ecg_data'], expected_output)

    def test_feature_extraction(self):

        # Calling the preprocess_ecg function
        processed_data = preprocess_ecg({'ecg_data': ecg_data})

        # Checking if expected features are present and have reasonable values
        self.assertIn('features', processed_data)
        # We can add other assertions to check feature values here