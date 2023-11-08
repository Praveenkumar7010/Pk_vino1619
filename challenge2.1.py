#Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality. 
class BankAccount:
  """A class to represent a bank account."""

  def __init__(self, account_number: int, account_holder_name: str, account_balance: float):
    """Initializes a new BankAccount object.

    Args:
      account_number: The account number.
      account_holder_name: The account holder name.
      account_balance: The account balance.
    """

    self._account_number = account_number
    self._account_holder_name = account_holder_name
    self._account_balance = account_balance

  def deposit(self, amount: float):
    """Deposits money into the account.

    Args:
      amount: The amount of money to deposit.
    """

    self._account_balance += amount

  def withdraw(self, amount: float):
    """Withdraws money from the account.

    Args:
      amount: The amount of money to withdraw.
    """

    if amount > self._account_balance:
      raise ValueError("Insufficient funds.")

    self._account_balance -= amount

  def get_balance(self) -> float:
    """Returns the account balance.

    Returns:
      The account balance.
    """

    return self._account_balance


def main():
  # Create a new BankAccount object.
  bank_account = BankAccount(1234567890, "John Doe", 1000.00)

  # Deposit $500.00 into the account.
  bank_account.deposit(500.00)

  # Withdraw $200.00 from the account.
  bank_account.withdraw(200.00)

  # Get the account balance.
  account_balance = bank_account.get_balance()

  # Print the account balance.
  print(f"Account balance: ${account_balance:.2f}")


if __name__ == "__main__":
  main()
#Account balance: $1300.00
