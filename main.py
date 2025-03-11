import datetime


class Amount:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.timestamp = datetime.datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} at {self.timestamp}"


class PersonalAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        transaction = Amount(amount, "DEPOSIT")
        self.transactions.append(transaction)
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds to withdraw")
        else:
            transaction = Amount(amount, "WITHDRAWAL")
            self.transactions.append(transaction)
            self.balance -= amount

    def print_transaction_history(self):
        if not self.transactions:
            print("No transactions found")
        else:
            for transaction in self.transactions:
                print(transaction)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"


def main():
    print("Welcome to the bank account system!")
    account_number = int(input("Enter your account number: "))
    account_holder = input("Enter your name: ")

    account = PersonalAccount(account_number, account_holder)

    while True:
        print("\nWhat would you like to do?")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Print transaction history")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            deposit_amount = float(input("Enter the amount to deposit: "))
            account.deposit(deposit_amount)
            print(f"Deposited {deposit_amount}. New balance: {account.get_balance()}")

        elif choice == '2':
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(withdraw_amount)
            if withdraw_amount <= account.get_balance():
                print(f"Withdrew {withdraw_amount}. New balance: {account.get_balance()}")

        elif choice == '3':
            print(f"Your current balance is: {account.get_balance()}")

        elif choice == '4':
            account.print_transaction_history()

        elif choice == '5':
            print("Thank you for using the bank account system!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
