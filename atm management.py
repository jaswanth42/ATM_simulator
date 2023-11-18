class ATM:
    def __init__(self, card_number, pin, balance=0):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"${amount} deposited. Your new balance is ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"${amount} withdrawn. Your new balance is ${self.balance}"
        else:
            return "Insufficient funds. Withdrawal failed."


def authenticate_user():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        card_number = input("Enter your card number: ")
        pin = input("Enter your PIN: ")

        # In a real-world scenario, you'd likely check the entered details against a database.
        # For simplicity, we'll use a hardcoded card number and PIN.
        if card_number == "123456789" and pin == "1234":
            return True
        else:
            print("Authentication failed. Incorrect card number or PIN.")
            attempts += 1

    print("Too many incorrect attempts. Exiting.")
    return False


def main():
    while True:
        if not authenticate_user():
            return

        atm = ATM(card_number="123456789", pin="1234")

        while True:
            print("\nATM Simulator\n")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            print("5. Change User (Re-enter Card Details)")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                print(atm.check_balance())
            elif choice == "2":
                amount = float(input("Enter the deposit amount: $"))
                print(atm.deposit(amount))
            elif choice == "3":
                amount = float(input("Enter the withdrawal amount: $"))
                print(atm.withdraw(amount))
            elif choice == "4":
                print("Exiting ATM. Thank you!")
                return
            elif choice == "5":
                break  # Go back to the authentication loop to change the user
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
