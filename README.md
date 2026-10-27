ATM Banking System
A simple, menu-driven ATM Banking System built using Python to manage a basic account balance and record transactions.
About
This project is a console-based application that simulates basic ATM operations. Users can check their current balance, deposit money, withdraw money, and view their transaction history.
The system starts with an initial balance of Rs. 10,000 and updates the balance whenever money is deposited or withdrawn.
Features
Check current account balance
Deposit money
Withdraw money
Prevent deposits of zero or negative amounts
Prevent withdrawals of zero or negative amounts
Check for insufficient balance before withdrawal
Record deposit and withdrawal transactions
Display transaction history
Handle invalid menu choices
Exit the program safely
Technologies Used
Python
Python Concepts Practiced
Variables and data types
Lists
Functions
while loops
for loops
Conditional statements
User input using input()
Type conversion using float()
Global variables
List methods such as append()
F-strings
Arithmetic operations
Input validation
How It Works
1. Check Balance
Displays the current account balance.
2. Deposit Money
Allows the user to enter an amount to deposit. The amount must be greater than zero. The system updates the balance and records the transaction.
3. Withdraw Money
Allows the user to withdraw money if the amount is greater than zero and does not exceed the available balance. The system updates the balance and records the transaction.
4. Show Transaction History
Displays all recorded deposits and withdrawals. If there are no transactions, the system displays a message.
Initial Balance
The account starts with Rs. 10,000.
Menu Options
Option
Function
0
Exit
1
Check Balance
2
Deposit Money
3
Withdraw Money
4
Show Transaction History

How to Run
Download or clone this repository.
Open the project folder in a code editor.
Make sure Python is installed.
Run the Python file:
python ATM_Banking_System.py
Data Storage
The account balance is stored in a variable, and transaction history is stored in a list. The data is kept in memory, so the balance and transaction history reset when the program restarts.
Purpose
This project is designed to practice Python fundamentals by building a simple ATM banking simulation.
Future Improvements
Add a PIN verification system
Save transaction history to a file
Support multiple bank accounts
Add transaction dates and times
Improve input validation
Add a graphical user interface
Author
Fatima Aziz
GitHub: fatimaaziz27
