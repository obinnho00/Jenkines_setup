import unittest
import xmlrunner
from app import (
    is_valid_email,
    mask_card_number,
    get_user_by_id,
    calculate_discount
)

class TestApp(unittest.TestCase):

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("not-an-email"))

    def test_mask_card_number(self):
        self.assertEqual(mask_card_number("1234567812345678"), "************5678")
        self.assertEqual(mask_card_number(987654321), "*****4321")
        with self.assertRaises(ValueError):
            mask_card_number("123")

    def test_get_user_by_id(self):
        users = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
        self.assertEqual(get_user_by_id(1, users)['name'], "Alice")
        self.assertIsNone(get_user_by_id(3, users))

    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(100, 10), 90)
        self.assertEqual(calculate_discount(250, 0), 250)
        with self.assertRaises(ValueError):
            calculate_discount(100, 150)
            
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))