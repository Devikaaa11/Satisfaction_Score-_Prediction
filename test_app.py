import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home_page(self):
        """
        Test if the home page renders correctly.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Satisfaction Score Prediction", response.data)

    def test_predict_valid_input(self):
        """
        Test prediction route with valid inputs.
        """
        response = self.client.post('/predict', data={
            "Items Purchased": "5",
            "Warranty Extension": "yes",
            "Loyalty Score": "30"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Prediction Result", response.data)
