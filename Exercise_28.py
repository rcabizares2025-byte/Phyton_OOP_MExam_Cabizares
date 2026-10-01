class BankAccount:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self._balance:
            raise ValueError
        self._balance -= amount


account = BankAccount(100)
account.deposit(50)
account.withdraw(20)

print(account.get_balance())