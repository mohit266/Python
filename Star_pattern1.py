
inp = int(input("How many rows you want to print:"))
n = inp+1
for i in range(n-1, 0, -1):
    for j in range(1, n-i):
        print("", end=" ")
    for j in range(1, i+1):
        print("", end="*")
    print("\r")


