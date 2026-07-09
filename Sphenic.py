def Check_Prime(x):
    c=0
    for i in range(2, (x//2)+1):
        if x%i==0:
            c+=1
    return True if c==0 else False
    
print("A Sphenic Number is a positive integer which has exactly three Prime Factors.\n Example: 30, 42, 66, 70 , 78, etc")
n=int(input("Enter a number to check for Sphenic Number: "))
count=0
for j in range(2, (n//2)+1):
    if n%j==0:
        result=Check_Prime(j)
        if result:
            count+=1
print(n, " is a Sphenic Number.") if count==3 else print(n, " is NOT a Sphenic Number.")