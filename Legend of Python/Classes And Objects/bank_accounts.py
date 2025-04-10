class BankAccount:
    def __init__(self, firstName, lastName, account_id, account_type, pin, balance):
        self.firstName = firstName
        self.lastName = lastName
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
    def deposit(self, amount):
            self.balance = self.balance + amount
            print(f"Monney added to account. New balance: " , self.balance)
    def withdraw(self, amount):
            self.balance = self.balance - amount
            print(f"Extracted money from account. New balance: " , self.balance)
    def display_balance(self):
        print("Your current balance is:" , self.balance)

user1 = BankAccount("Junior", "Jimenez", 2343, "Personal", 4914, 100)
user2 = BankAccount("Frank", "Jimenez", 8489, "Busines", 9174, 50)

user1.display_balance()
user1.deposit(100)
user2.withdraw(10)
