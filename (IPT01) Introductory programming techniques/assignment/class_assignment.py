class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        # Initialize a BankAccount object with account_number, account_holder, and balance attributes
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # Method to deposit money into the account
        self.balance += amount
        return f"Deposit of {amount} successful. Current balance: {self.balance}"

    def withdraw(self, amount):
        # Method to withdraw money from the account
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of {amount} successful. Current balance: {self.balance}"
        else:
            return "Insufficient funds"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.05):
        # Initialize a SavingsAccount object with account_number, account_holder, balance, and interest_rate attributes
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        # Method to add interest to the savings account balance
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest of {interest} added. Current balance: {self.balance}"


# Test cases
def test_bank_account():
    # Test cases for the BankAccount class
    account = BankAccount("123456", "John Doe")
    assert account.deposit(100) == "Deposit of 100 successful. Current balance: 100"
    assert account.withdraw(50) == "Withdrawal of 50 successful. Current balance: 50"
    assert account.withdraw(60) == "Insufficient funds"


def test_savings_account():
    # Test cases for the SavingsAccount class
    savings_account = SavingsAccount("987654", "Jane Smith")
    assert savings_account.deposit(500) == "Deposit of 500 successful. Current balance: 500"
    assert savings_account.add_interest() == "Interest of 25.0 added. Current balance: 525.0"
    assert savings_account.withdraw(100) == "Withdrawal of 100 successful. Current balance: 425.0"


if __name__ == "__main__":
    # Instantiate objects
    account = BankAccount("123456", "John Doe")
    savings_account = SavingsAccount("987654", "Jane Smith")

    # Demonstrate methods
    print(account.deposit(100))
    print(account.withdraw(50))

    print(savings_account.deposit(500))
    print(savings_account.add_interest())
    print(savings_account.withdraw(100))

    # Test cases
    test_bank_account()
    test_savings_account()
    print("All tests passed!")
