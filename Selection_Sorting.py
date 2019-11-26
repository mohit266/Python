list = []

list_size = int(input("Enter the size of list : "))
for i in range(list_size):
    user_input = int(input(f"Enter {i+1} number : "))
    list.append(user_input)

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]

print(f"Sorted list is  {list}")
