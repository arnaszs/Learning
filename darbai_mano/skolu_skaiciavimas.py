import unittest
from debt import LoanCalculator

class TestLoanCalculator(unittest.TestCase):
    def setUp(self):
        self.obj = LoanCalculator()
        self.obj.get_monthly_payment(10000, 5, 5)
        self.obj.get_monthly_payment(10000, 10, 5)
        self.obj.get_monthly_payment(10000, 2.5, 5)

    def test_payment_up(self):
        self.assertAlmostEqual(self.obj.monthly_payment(10000, 10, 5), 212.47, 2)

    def test_payment_down(self):
        self.assertAlmostEqual(self.obj.monthly_payment(10000, 2.5, 5), 177.47, 2)

if __name__ == '__main__':
    unittest.main()

