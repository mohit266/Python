
while(4>1):
    n = int(input("How many rows you want to print:"))
    one = int(input("Enter 1 for True and 0 for false and q for quit:"))
    new = bool(one)
    if new==True:
        for i in range(1,n+1):
            for j in range(1,i+1):
                print("*",end="")
            print("\r")
    elif new==False:
        for i in range(n,0,-1):
            for j in range(1,i+1):
                print("*", end="")
            print("\r")
