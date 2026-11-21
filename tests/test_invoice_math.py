import unittest

from invoice_math import add_tax, apply_discount


class TestInvoiceMath(unittest.TestCase):
    def test_add_tax(self):
        self.assertEqual(add_tax(100, 18), 118.0)

    def test_apply_discount(self):
        self.assertEqual(apply_discount(100, 10), 90.0)

    def test_apply_discount_zero_and_full(self):
        self.assertEqual(apply_discount(100, 0), 100.0)
        self.assertEqual(apply_discount(100, 100), 0.0)


if __name__ == "__main__":
    unittest.main()
