list = []

user_input = int(input("Enter the size of list : "))
for i in range(user_input):
    list_input = int(input(f"Enter {i+1} number : "))
    list.append(list_input)

for i in range(1, len(list)):
    key = list[i]
    # print(key)
    j = i - 1
    while j >= 0 and key < list[j]:
        list[j + 1] = list[j]
        j -= 1
    list[j + 1] = key
print(list)