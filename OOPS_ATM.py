class ATM:
    def __init__(self):
        print("\nWelcome to ATM")
        print("----------------------------------")
        while True:
            self.atm_cash = int(input("Enter cash available in ATM (multiple of 1000): "))
            if self.atm_cash % 1000 == 0:
                break
            print("Cash must be in multiples of 1000.\n")
        self.user_amt = int(input("Enter your Bank Balance: "))
        self.pin = int(input("Set your PIN: "))

        # Daily withdrawal limit
        self.withdraw_limit = 25000
        self.total_withdrawn = 0
        print("\nATM Started Successfully!")

    # Verify PIN
    def verify_pin(self):
        check_pin = int(input("Enter your PIN: "))
        return check_pin == self.pin

    # Receipt
    def receipt(self, transaction, amount):
        choice = input("Do you want a receipt? (Y/N): ").upper()

        if choice == "Y":
            print("\n----------- RECEIPT -----------")
            print("Transaction :", transaction)
            print("Amount      :", amount)
            print("Balance     :", self.user_amt)
            print("-------------------------------")

    # Balance Enquiry
    def balance_enquiry(self):
        if self.verify_pin():
            print("\nCurrent Bank Balance =", self.user_amt)
        else:
            print("Incorrect PIN!")

    # Cash Deposit
    def cash_deposit(self):
        if not self.verify_pin():
            print("Incorrect PIN!")
            return
        deposit = int(input("Enter amount to deposit: "))
        self.user_amt += deposit
        self.atm_cash += deposit
        print("Deposit Successful.")
        self.receipt("Cash Deposit", deposit)

    # Cash Withdrawal
    def cash_withdrawal(self):
        if not self.verify_pin():
            print("Incorrect PIN!")
            return

        amount = int(input("Enter amount to withdraw: "))

        # Withdrawal Limit
        if self.total_withdrawn + amount > self.withdraw_limit:
            print("Daily Withdrawal Limit Exceeded!")
            return
        if amount > self.user_amt:
            print("Insufficient Bank Balance!")
            return
        if amount > self.atm_cash:
            print("ATM does not have sufficient cash!")
            return

        # ATM has only 500 and 200 notes
        if amount % 100 != 0 or amount == 100 or amount == 300:
            print("ATM can dispense only Rs.500 and Rs.200 notes.")
            return

        self.user_amt -= amount
        self.atm_cash -= amount
        self.total_withdrawn += amount
        print("Please collect your cash.")
        self.receipt("Cash Withdrawal", amount)

    # PIN Change
    def pin_change(self):
        if not self.verify_pin():
            print("Incorrect PIN!")
            return
        while True:
            new_pin = int(input("Enter New PIN: "))
            confirm = int(input("Confirm New PIN: "))
            if new_pin == confirm:
                self.pin = new_pin
                print("PIN Changed Successfully.")
                break
            else:
                print("PIN does not match. Try Again.")

    # Display ATM Details
    def atm_status(self):
        print("\n----- ATM STATUS -----")
        print("Cash Available in ATM :", self.atm_cash)
        print("----------------------")

    # Main Menu
    def menu(self):
        while True:
            print("\n========= ATM MENU =========")
            print("1. Balance Enquiry")
            print("2. Cash Deposit")
            print("3. Cash Withdrawal")
            print("4. PIN Change")
            print("5. ATM Cash Status")
            print("6. Exit")
            print("============================")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.balance_enquiry()
            elif choice == 2:
                self.cash_deposit()
            elif choice == 3:
                self.cash_withdrawal()
            elif choice == 4:
                self.pin_change()
            elif choice == 5:
                self.atm_status()
            elif choice == 6:
                print("\nThank You for using ATM!")
                break
            else:
                print("Invalid Choice! Try Again.")

atm = ATM()
atm.menu()