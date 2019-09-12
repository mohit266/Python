import random

lst = ['s', 'w', 'g']

print(" Game : Snake, Water, Gun")

Total_chance = 10
Human_points = 0
Computer_points = 0
No_of_chance = 0
print(" s for snake \n w for water \n g for gun\n")
while Total_chance > No_of_chance:
    user_input = input("Enter your choice : ")
    computer_input = random.choice(lst)

    # if human and computer both chooses same option
    if user_input.lower() == computer_input:
        print(f"\tYour guess {user_input} and Computer guess {computer_input}")
        print("\tGame tied !! Please try again")

    if user_input.lower() == 's' and computer_input == 'w':
        Human_points += 1
        print(f"\tYour guess {user_input} and computer guess {computer_input} is : ", Human_points)
        print(f"\tYou wins and Computer loss")
        print(f"\tYour points is {Human_points}")

    elif user_input.lower() == 's' and computer_input == 'g':
        Computer_points += 1
        print(f"\tyour guess {user_input} and computer guess {computer_input} ")
        print(f"\tComputer wins and You loss")
        print(f"\tComputer points is {Computer_points}")

    elif user_input.lower() == 'w' and computer_input == 's':
        Computer_points += 1
        print(f"\tyour guess {user_input} and computer guess {computer_input}")
        print(f"\tComputer wins and You loss")
        print(f"\tcomputer points is {Computer_points}")

    elif user_input.lower() == 'w' and computer_input == 'g':
        Human_points += 1
        print(f"\tYour guess {user_input} and computer guess {computer_input}")
        print(f"\tYou wins and Computer loss")
        print(f"\tYour points is {Human_points}")

    elif user_input.lower() == 'g' and computer_input == 'w':
        Computer_points += 1
        print(f"\tyour guess {user_input} and computer guess {computer_input}")
        print(f"\tComputer wins and You loss")
        print(f"\tcomputer points is {Computer_points}")

    elif user_input.lower() == 'g' and computer_input == 's':
        Human_points += 1
        print(f"\tYour guess {user_input} and computer guess {computer_input}")
        print(f"\tYou wins and Computer loss")
        print(f"\tYour points is {Human_points}")

    else:
        print("\tPlease enter valid input")

    No_of_chance += 1
    Total_chance_left = Total_chance - No_of_chance
    print(f"\tNumber of chances left is {Total_chance_left}")
    print(f"\tHuman points is {Human_points}")
    print(f"\tComputer points is {Computer_points}")

print("\tGame Over")

if Computer_points > Human_points:
    print(f"\tComputer wins by {Computer_points-Human_points}")

if Human_points > Computer_points:
    print(f"\tYou win by {Human_points-Computer_points}")

print(f"\tYour points is {Human_points} and computer points is {Computer_points}")

