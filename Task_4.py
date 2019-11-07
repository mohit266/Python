try:
    n = int(input("Enter number of apples : "))
    mn = int(input("Enter minimum range : "))
    mx = int(input("Enter maximum range : "))

except ValueError:
    print("Enter Integers only.")
    exit()

if mn >= mx:
    print("This can not be the range as the min should be less than max")

for i in range(mn, mx+1):
    if n % i == 0:
        print(f"{i} is divisor of {n}")

    else:
        print(f"{i} is not a divisor of {n}")