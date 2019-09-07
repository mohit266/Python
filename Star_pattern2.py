
while(1):
    n = int(input("Enter how many rows you want to print:"))
    for i in range(1, n):
        for j in range(1, n-i):
            print(" ", end="")
        for j in range(1,i+1):
            print("*", end="")
        print("\r")
