class Account:
    def __init__(self, account_number, account_holder, pin, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance
        self.transactions = []  

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ${amount:.2f}")
            return f"Deposited: ${amount:.2f}. New Balance: ${self.balance:.2f}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount:.2f}")
            return f"Withdrawn: ${amount:.2f}. Remaining Balance: ${self.balance:.2f}"
        return "Insufficient funds or invalid amount."

    def check_balance(self):
        return f"Current Balance: ${self.balance:.2f}"

    def mini_statement(self):
        statement = "Mini Statement:\n"
        statement += "\n".join(self.transactions[-5:]) 
        return statement if self.transactions else "No transactions yet."


class ATM:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_number, account_holder, pin):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, account_holder, pin)
            return "Account created successfully."
        return "Account number already exists."
    
    def authenticate_user(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        return None

    def display_menu(self):
        print("\n----- ATM Menu -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Mini Statement")
        print("5. Exit")


def main():
    atm = ATM()

    
    atm.create_account("12345", "Alice Smith", "1234")
    atm.create_account("67890", "Bob Johnson", "5678")

    
    atm.accounts["12345"].balance = 1000  
    atm.accounts["67890"].balance = 500    

    print("Welcome to the ATM!")
    
    while True:
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        
        account = atm.authenticate_user(account_number, pin)
        if account:
            print(f"\nWelcome, {account.account_holder}!")
            while True:
                atm.display_menu()
                choice = input("Select an option: ")
                
                if choice == '1':
                    print(account.check_balance())
                elif choice == '2':
                    amount = float(input("Enter amount to deposit: "))
                    print(account.deposit(amount))
                elif choice == '3':
                    amount = float(input("Enter amount to withdraw: "))
                    print(account.withdraw(amount))
                elif choice == '4':
                    print(account.mini_statement())
                elif choice == '5':
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid selection. Please try again.")
            break
        else:
            print("Authentication failed. Please check your account number and PIN.")

if __name__ == "__main__":
    main()
