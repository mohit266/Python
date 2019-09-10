def getdate():
    import datetime
    return datetime.datetime.now()

print("Health Management System")

n = int(input(" 1.log \n 0 To retrieve the data \n Enter your choice:"))
if n == 1:
    a = int(input(" 1.Rohan \n 2.Maan \n 3.Anurag \n Enter your choice:"))
    if a == 1:
        b= int(input("Enter 1 for exercise and 0 for food:"))
        if b == 1:
            f = open("Rohan_Exercise.txt", 'a')
            exercise_inp = input("Enter the exercise:")
            f.write((str([str(getdate())])) + ":" + exercise_inp + "\n")
            print("Successfully added")
            f.close()

        elif b == 0:
            food_inp = input("Enter your meal:")
            f = open("Rohan_Food.txt", 'a')
            f.write((str([str(getdate())])) + ":" + food_inp + "\n")
            print("Successfully added")
            f.close()

        else:
            print("Please enter valid input")

    elif a == 2:
        b = int(input("Enter 1 for exercise and 0 for food:"))
        if b == 1:
            f = open("Maan_Exercise.txt", 'a')
            exercise_inp = input("Enter you exercise:")
            f.write((str([str(getdate())])) + ":" + exercise_inp + "\n")
            print("Successfully added")
            f.close()

        elif b == 0:
            f = open("Maan_Food.txt", 'a')
            food_inp = input("Enter you meal:")
            f.write((str([str(getdate())])) + ":" + food_inp + "\n")
            print("Successfully added")
            f.close()

        else:
            print("Enter valid input")

    elif a == 3:
        b = int(input("Enter 1 for exercise and 0 for food:"))
        if b == 1:
            f = open("Anurag_Exercise.txt", 'a')
            exercise_inp = input("Enter the exercise:")
            f.write((str([str(getdate())])) + ":" + exercise_inp + "\n")
            print("Successfully added")
            f.close()

        elif b == 0:
            food_inp = input("Enter your meal:")
            f = open("Anurag_Food.txt", 'a')
            f.write((str([str(getdate())])) + ":" + food_inp + "\n")
            print("Successfully added")
            f.close()

        else:
            print("Please enter valid input")

    else:
        print("Enter valid input")

elif n == 0:
    a = int(input(" 1.Rohan \n 2.Maan \n 3.Anurag \n Enter your choice:"))
    if a == 1:
        b = int(input("Enter 1 for exercise and 0 for food:"))
        if b == 1:
            f = open("Rohan_Exercise.txt")
            excercise_read = f.read()
            print(excercise_read)
            f.close()

        elif b == 0:
            f = open("Rohan_Food.txt")
            food_read = f.read()
            print(food_read)
            f.close()

        else:
            print("Please Enter valid input")

    if a == 2:
        b = int(input("Enter 1 for exercise and 0 for food:"))
        if b == 1:
            f = open("Maan_Exercise.txt")
            excercise_read = f.read()
            print(excercise_read)
            f.close()

        elif b == 0:
            f = open("Maan_Food.txt")
            food_read = f.read()
            print(food_read)
            f.close()

        else:
            print("Please Enter valid input")

    if a == 3:
        b = int(input("Enter 1 for exercise and 0 for food:"))
        if b == 1:
            f = open("Anurag_Exercise.txt")
            excercise_read = f.read()
            print(excercise_read)
            f.close()

        elif b == 0:
            f = open("Anurag_Food.txt")
            food_read = f.read()
            print(food_read)
            f.close()

        else:
            print("Please Enter valid input")

    else:
        print("Please Enter valid input")

else:
    print("Please enter valid input")