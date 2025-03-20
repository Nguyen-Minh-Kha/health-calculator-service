import unittest
import json
from app import app
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_calculate_bmi(self):
        # Will fail if BMI formula is incorrect: weight(kg)/(height(m))^2
        # Common error: using wrong units or incorrect formula structure
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        self.assertAlmostEqual(calculate_bmi(1.80, 80), 24.69, places=2)
        self.assertAlmostEqual(calculate_bmi(1.60, 50), 19.53, places=2)
    
    def test_calculate_bmr_male(self):
        # Will fail if male BMR formula is incorrect
        # Common error: height should be in cm here (175cm), not meters
        # Formula: 88.362 + (13.397 × weight) + (4.799 × height) - (5.677 × age)
        self.assertAlmostEqual(calculate_bmr(175, 70, 30, 'male'), 1695.67, places=2)
    
    def test_calculate_bmr_female(self):
        # Will fail if female BMR formula is incorrect
        # Common error: using male formula or incorrect coefficients
        # Formula: 447.593 + (9.247 × weight) + (3.098 × height) - (4.330 × age)
        self.assertAlmostEqual(calculate_bmr(165, 55, 25, 'female'), 1359.10, places=2)
    
    def test_bmi_endpoint(self):
        # Will fail if:
        # 1. /bmi endpoint doesn't exist or doesn't accept POST requests
        # 2. JSON parsing is incorrect
        # 3. BMI category logic differs (under 18.5: Underweight, 18.5-25: Normal, etc.)
        response = self.app.post('/bmi',
                                json={'height': 1.75, 'weight': 70},
                                content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(data['bmi'], 22.86, places=2)
        self.assertEqual(data['category'], 'Normal weight')

    def test_bmr_endpoint_male(self):
        # Will fail if:
        # 1. /bmr endpoint doesn't exist or doesn't accept POST requests
        # 2. Response format is different than expected
        # 3. Gender parameter handling is case-sensitive or different than expected
        response = self.app.post('/bmr',
                                json={'height': 175, 'weight': 70, 'age': 30, 'gender': 'male'},
                                content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(data['bmr'], 1695.67, places=2)

if __name__ == '__main__':
    unittest.main()