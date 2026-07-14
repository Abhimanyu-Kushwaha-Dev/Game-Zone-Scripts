print("\n======= PASCAL'S TRIANGLE =======\n")
n = int(input("Enter the number of rows: "))
for i in range(n):
    print("  "*(n-i-1), end="")
    value=1
    for j in range(i+1):
        print(f"{value:4}", end="")
        value=value*(i-j)//(j+1)
    print()