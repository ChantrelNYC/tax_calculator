import unittest
from src.cart import apply_discount, calculate_tax

class TestShoppingCart(unittest.TestCase):

    def test_apply_discount_logic(self):
        # This passes on the buggy code (100 - 20 = 80, and 100 * 0.8 = 80)
        # This tricks the student into thinking it works if they only test 100.
        self.assertEqual(apply_discount(100, 20), 80.0)

        # This FAILS on the buggy code.
        # Current code: 50 - 20 = 30
        # Correct math: 50 * (1 - 0.20) = 40
        self.assertEqual(apply_discount(50, 20), 40.0, 
            "Math Error: A 20% discount on $50 should result in $40, not $30!")

    def test_calculate_tax(self):
        # Fails because function returns 0
        self.assertEqual(calculate_tax(100, 0.05), 5.0, "Tax function is not implemented!")
        self.assertEqual(calculate_tax(50, 0.10), 5.0)

if __name__ == '__main__':
    unittest.main()