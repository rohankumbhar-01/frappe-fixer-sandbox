import unittest

from invoice_math import add_tax


class TestInvoiceMath(unittest.TestCase):
    def test_add_tax(self):
        self.assertEqual(add_tax(100, 18), 118.0)


if __name__ == "__main__":
    unittest.main()
