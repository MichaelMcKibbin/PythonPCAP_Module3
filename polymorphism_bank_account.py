class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        opening_balance = self.__balance
        if self._credit(amount):
            print(f"Opening Balance 1: {opening_balance} Deposited {amount}. New balance: {self.__balance}")

    def _credit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            print("Deposit amount must be positive.")
            return False

    def withdrawal(self, amount):
        print("Opening Balance 2:", self.__balance)
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")

    def get_balance(self):
        return self.__balance


b1 = BankAccount("012345678", 1000)

b1.deposit(500)
b1.withdrawal(200)
print(f"Current balance 1: {b1.get_balance()}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdrawal(self, amount):
        if 0 < amount <= (self.get_balance() + self.overdraft_limit):
            new_balance = self.get_balance() - amount
            if new_balance < 0:
                print(f"Overdraft limit exceeded. Current balance 3: {self.get_balance()}, Overdraft limit: {self.overdraft_limit}")
            else:
                super().withdrawal(amount)
        else:
            print("Withdrawal amount must be positive and within the overdraft limit.")

current_account = CurrentAccount("123456789", 1000, 500)
current_account.deposit(500)
current_account.withdrawal(200)
print("Test overdraft limit...")
current_account.withdrawal(2000)  # This should trigger the overdraft limit message


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            super().deposit(amount)
        else:
            print("Deposit amount must be positive.")

    def apply_interest(self):
        print("Opening Balance 3:", self.get_balance())
        interest = self.get_balance() * (self.interest_rate / 100)
        if interest < 0:
            print("Interest amount must not be negative.")
            return
        if interest > 0 and not self._credit(interest):
            return
        print(f"Account {self.account_number}: Interest of {interest} applied. New balance: {self.get_balance()}")


savings_account = SavingsAccount("987654321", 1000, 5)
savings_account.deposit(600)
savings_account.apply_interest()
