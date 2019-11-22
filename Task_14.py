list = []
list_input = int(input("Enter the size of list"))
for i in range(list_input):
    list_app = int(input(f"Enter {i+1} number :"))
    list.append(list_app)
print(list)

user_input = int(input("Enter any number to return largest number "))
a = 1

if user_input == 0:
    print("Please enter valid input")
else:
    while a < user_input:
        for i in list:
            if i == max(list):
                list.remove(i)
        a = a + 1
    print(f" {user_input} Largest number is : {max(list)}")


