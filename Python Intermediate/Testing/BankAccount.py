import unittest
from wealthManager import BankAccount 

class TestBankaccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(100)
    # A tearDown() method that sets the value of a BankAccount object to None.
    def tearDown(self):
        self.account = BankAccount(None)
    # testing the initial balance
    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)
    # deposit amount on bank account
    def test_deposit_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
    # error raiser for negative amount deposit
    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-40)

if __name__ == '__main__':
  unittest.main()