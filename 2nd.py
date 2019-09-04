# guessing the number
my_num = 26
guess = 1
print("Number of guesses is limited to 9 times only")
while (guess<=9):

    inp = int(input("Guess any number: "))

    if inp > my_num:
        print("You enter greater number !! Please input smaller number !!")

    elif inp < my_num:
        print("You enter smaller number !! Please input greater number ")

    else:
        print("Congrats!!You guess the right number")
        print("You guess the right number in ", guess, "attempt")
        break

    print(9-guess, "No. of guess left")
    guess = guess+1

if(guess>9):
    print("Game over")