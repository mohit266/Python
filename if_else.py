# ladder if else
'''
age = int(input("Enter your age : "))

# if condition will run only below 100 age
if age>18 and age<=100:
    print("You can drive")
elif age==18:
    print("We will think about you")
elif age>100:
    print("Enter valid input")
else:
    print("You cannot drive")
'''
# Faulty calculator

print("This calculator is developed by Mohit")
while 4>3:
    operator = input("+ for addition \n- for subtraction \n* for multiplication \n/ for modulus \nChoose any operation:")
    num1 = int(input("Enter your first number :"))
    num2 = int(input("Enter your second number :"))

    if num1==56 and num2==9 and operator=='+':
        print("Your result is : 77")
    elif num1==45 and num2==3 and operator=='*':
        print("Your result is : 555")
    elif num1==56 and num2==6 and operator=='/':
        print("Your result is :4")
    elif operator=='+':
        print("Addition of two numbers is:",num1+num2)
    elif operator=='-':
        print("Subtraction of two numbers is:",num1-num2)
    elif operator=='*':
        print("Multiplication of two number is:",num1*num2)
    elif operator=='/':
        print("Modulus of two number is:",num1/num2)