a = input("Enter your name : ")
b = int(input("How much do you earn : "))

if b==0:
    raise ZeroDivisionError("b is zero so stopping the program")
if a.isnumeric():
    raise Exception("Number are not allowed")

print(f"Hello {a}")