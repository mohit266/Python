# Program which will keep adding stream of numbers inputted by the user.

lst =[]
sum = 0
while True:
    user_input = input("Enter the item price and press q for exit: \n")
    if user_input != 'q':
        sum = sum + int(user_input)
        lst.append(sum)
        print(f"Order total so far {sum}")
    else:
        for index, item in enumerate(lst):
            print(f"{index+1}.Rs{item}")
        print(f"Your Bill total is {sum}. Thanks for shopping with us. ")
        break
