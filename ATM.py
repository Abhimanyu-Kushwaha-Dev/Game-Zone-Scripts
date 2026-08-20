"""
Features:
balance inquiry
cash withdrawal (in 500 and 200 only)
PIN change
Deposit
withdrawal limit------
receipt option--------
"""

def Prepare():
    print()
    global pin, user_amt
    print("welcome to ATM")
    print("Before using the ATM, kindly enter the following details: ")
    cash=int(input(("Enter max cash in this ATM (cash must be a multiple of 1000): ")))
    if cash%1000 !=0:
        print("Kindly enter the cash in multiple of 1000 only")
        Prepare()
    user_amt=int(input(("Enter the amount you already have in your bank account: ")))
    pin=int(input("Enter your PIN: "))
    print("Now we shall start the ATM")
    ATM()

def Balance_Enquiry():
    print()
    global pin, user_amt
    check_pin=int(input("Enter your PIN: "))
    if check_pin==pin: 
        print("Your current Bank Balance is: ", user_amt)
    else:
        print("Entered pin is Incorrect! \n Redirecting to Home Page.")
        ATM()

    
def Cash_Deposit():
    print()
    global pin, user_amt
    check_pin=int(input("Enter your PIN: "))
    if check_pin==pin: 
        deposit=int(input("Enter the amount you want to Deposit: "))
        user_amt=user_amt+deposit
        flag=int(input("Do you want to see your Bank Balance (1 for Yes, 0 for No): "))
        if flag==1:
            Balance_Enquiry()    
        else:
            print("OK")
            ATM()
    else:
        print("Entered pin is Incorrect! \n Redirecting to Home Page.")
        ATM()
    
def Cash_Withdrawal():
    print()
    global pin, user_amt
    check_pin=int(input("Enter your PIN: "))
    if check_pin==pin: 
        withdraw=int(input("Enter the amount you want to Withdraw: "))
        if withdraw==100 or withdraw==300 or (withdraw%100)!=0:
            print(f"ATM cannot dispence {withdraw} with 200 or 500 Ruppee Notes. \n Redirecting to Home Page.")
            ATM()
        else:
            print("Cash Dispensed Successfully.")
            user_amt=user_amt-withdraw

        flag=int(input("Do you want to see your Bank Balance (1 for Yes, 0 for No): "))
        if flag==1:
            Balance_Enquiry()    
        else:
            print("OK")
            ATM()
    else:
        print("Entered pin is Incorrect! \n Redirecting to Home Page.")
        ATM()

def PIN_Change():
    print()
    check_pin=int(input("Enter your Old PIN: "))
    if check_pin==pin: 
        new_pin=int(input("Enter the new PIN: "))
        pin=new_pin
        ATM()
    else:
        print("Entered pin is Incorrect! \n Redirecting to Home Page.")
        ATM()

def ATM():
    while True:
        print()
        print("We have the following features with us:")
        print("1) Balance Enquiry: ")
        print("2) Cash Deposit: ")
        print("3) Cash Withdrawal(500 and 200 available only): ")
        print("4) PIN change: ")
        print("5) Exit")
        print()
        ch=int(input("Enter your choice: "))
        if ch==1:
            Balance_Enquiry()
        elif ch==2:
            Cash_Deposit()
        elif ch==3:
            Cash_Withdrawal()
        elif ch==4:
            PIN_Change()
        elif ch==5:
            print("Thank You for using ATM!")
            break
        else:
            print("Invalid Choice!")
            ATM()
            print()
        print()

Prepare()