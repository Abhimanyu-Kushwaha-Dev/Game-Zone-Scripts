def Decimal_to_Binary():
    try:
        decimal = int(input("Enter a decimal number: "))
        if decimal<=0:
            print("Negative number found.")
        elif decimal == 0:
            print("Binary:", 0)
        else:
            binary = ""
            while decimal > 0:
                binary = str(decimal % 2) + binary
                decimal //= 2
            print("Binary:", binary)
        print()
    except Exception:
        print("Invalid Input!\n")

def Binary_to_Decimal():
    try:
        binary = input("Enter a binary number: ")
        valid = True
        for digit in binary:
            if digit != '0' and digit != '1':
                valid = False
                break
        if not valid:
            print("Error: Please enter a valid binary number (only 0s and 1s are allowed).")
            Binary_to_Decimal()
        else:
            decimal = 0
            power = 0
            for digit in binary[::-1]:
                decimal += int(digit) * (2 ** power)
                power += 1
            print("Decimal:", decimal)
            print()
    except Exception:
        print("Invalid Input!\n")

def main():
    while(True):    
        print("Decimal <--> Binary Converter")
        print("Enter 1 to Use Decimal to Binary converter")
        print("Enter 2 to Use Binary to Decimal converter")
        print("Enter 0 to Exit")
        try:
            choice=int(input("Enter your Choice: "))
            if choice==1:
                Decimal_to_Binary()
            elif choice==2:
                Binary_to_Decimal()
            elif choice==0:
                print("Bye-Bye!!")
                break
            else:
                print("Invalid Input!\n")
        except Exception:
            print("Invalid Input!\n")
            
main()