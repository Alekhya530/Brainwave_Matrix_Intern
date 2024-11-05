#ATM Interface Program
This Python program simulates a simple ATM interface, allowing users to create and manage bank accounts, make deposits, withdraw funds, check balances, and view a mini statement of recent transactions. This is a fully functional ATM simulation with authentication, balance management, and transaction tracking.

Table of Contents
Features
Classes
Setup
Usage
Example Workflow
Future Enhancements
Features
Account Creation: Create new bank accounts with unique account numbers.
Authentication: Users authenticate with an account number and a PIN.
Balance Check: Users can check their current balance.
Deposit and Withdrawal: Users can deposit or withdraw funds with balance validation.
Mini Statement: View the five most recent transactions.
Exit Option: Exit the ATM session safely.
Classes
Account
This class represents a user’s bank account and includes:

Attributes:
account_number: The unique identifier for the account.
account_holder: The name of the account holder.
pin: A PIN for authentication.
balance: Initial balance (default is 0).
transactions: A list of transactions for the mini statement.
Methods:
deposit(amount): Adds the specified amount to the balance if positive.
withdraw(amount): Deducts the specified amount from the balance if sufficient funds are available.
check_balance(): Returns the current balance.
mini_statement(): Returns the last five transactions.
ATM
This class simulates the ATM interface and operations:

Attributes:
accounts: A dictionary holding Account objects keyed by account numbers.
Methods:
create_account(account_number, account_holder, pin): Creates an account if the account number is not in use.
authenticate_user(account_number, pin): Authenticates a user based on account number and PIN.
display_menu(): Displays the ATM options menu.
Setup
To use this program:

Ensure Python is installed on your system.
Save the code to a file, e.g., atm_interface.py.
Usage
Run the program using:

bash
Copy code
python atm_interface.py
Example Workflow
Run the program.
Enter the account number and PIN to authenticate.
Select options from the menu to perform banking operations:
Check balance
Deposit funds
Withdraw funds
View a mini statement
Exit the program when done.
Future Enhancements
Potential improvements could include:

Account Persistence: Saving account data to a database or file.
Enhanced Security: Implementing secure hashing for PINs.
Multiple Transaction Statements: Display more than the last five transactions.
Internationalization: Support for multiple languages.
