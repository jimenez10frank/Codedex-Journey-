import unittest

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    # deposit function
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be Positive')
        self.balance += amount

    # withdraw function
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError('Insuffiecient Funds')
        self.balance -= amount

