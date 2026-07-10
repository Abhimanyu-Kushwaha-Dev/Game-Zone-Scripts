print("An Automorphic number is a natural number whose nth power ends with the exact same digits as the original number.")
n = int(input("Enter the value of n: "))
num = int(input("Enter a number to check: "))
check = num
count = 0

while check > 0:
    check //= 10
    count += 1

if (num ** n) % (10 ** count) == num:
    print(f"{num} is an Automorphic Number.")
else:
    print(f"{num} is NOT an Automorphic Number.")