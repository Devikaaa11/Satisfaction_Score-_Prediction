import unittest
from app import app

class TestIntegrationFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_complete_workflow(self):
        """
        Test the complete workflow from home page to prediction.
        """
        # Step 1: Access home page
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Satisfaction Score Prediction", response.data)

        # Step 2: Submit valid prediction data
        response = self.client.post('/predict', data={
            "Items Purchased": "10",
            "Warranty Extension": "yes",
            "Loyalty Score": "25"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Prediction Result", response.data)
