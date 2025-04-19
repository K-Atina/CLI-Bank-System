import time
import sys


def deposit(balance,new_deposit):
    if new_deposit>0:
        balance=balance+new_deposit
        time.sleep(0.8)
        print(f"You have successfully deposited ${new_deposit}")
        return balance
    else:
        print("You can't deposit negative numbers!")
        return balance

def check_balance(balance):
    print(f"You're current balance is ${balance}")
    
def withdraw_money(balance,new_withdraw):
    if new_withdraw>balance:
        print("You don't have enough money in your account!")
        return balance
    elif new_withdraw <= 0:
        print("Invalid amount. You must withdraw more than $0.")
        return balance
    else:
        balance=balance-new_withdraw 
        time.sleep(0.8) 
        print(f"You have successfully withdrawn ${new_withdraw}")
        return balance
    

def exit_program():
    time.sleep(2)
    print("Thank you for working with us")
    time.sleep(0.5)
    print("Bye!")
    sys.exit()
    
def type_out(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

          
#Main program function
def main():
    balance=0
    type_out("Welcome to the CLI Bank!")
    time.sleep(1)
    
    while True:
        type_out("\nWhat would you like to do?")
        time.sleep(0.5)
        type_out("1. Deposit")
        time.sleep(0.5)
        type_out("2. Withdraw")
        time.sleep(0.5)
        type_out("3. Check Balance")
        time.sleep(0.5)
        type_out("4. Exit")
        time.sleep(0.5)
        type_out("Enter your choice: ")
        
        choice = input()
        
        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                balance = deposit(balance, amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                balance = withdraw_money(balance, amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            check_balance(balance)

        elif choice == "4":
            exit_program()

        else:
            print("Invalid option. Please try again.")
            
if __name__ =="__main__":
    main()
