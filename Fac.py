# n! = n * n-1 * n-2 * n-3......1
# n! = n* (n-1)!
def Factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

number = int(input("Enter any number:"))
print(Factorial(number))