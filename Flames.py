def common(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                char = a[i]
                a.remove(char)
                b.remove(char)
                return (a + ["*"] + b, True)
    return (a + ["*"] + b, False)

# if __name__ == "__main__":
print("Inside Main")
n1 = list(input("Enter first name: ").lower().replace(" ", ""))
n2 = list(input("Enter Second name: ").lower().replace(" ", ""))
if not n1 or not n2:
    print("Please enter valid names.")
    exit()
flap = True
while flap:
    lst, flap = common(n1, n2)
    i = lst.index("*")
    n1 = lst[:i]
    n2 = lst[i + 1:]
c = len(n1) + len(n2)
options = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
while len(options) > 1:
    index = (c % len(options)) - 1
    if index >= 0:
        right = options[index + 1:]
        left = options[:index]
        options = right + left
    else:
        options.pop()
print("Relationship status:", options[0])