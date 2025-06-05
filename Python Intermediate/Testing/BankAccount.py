import unittest
from wealthManager import BankAccount 

class TestBankaccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(100)
    # A tearDown() method that sets the value of a BankAccount object to None.
    def tearDown(self):
        self.account = BankAccount(None)