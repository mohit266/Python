list = []
dict = {}

list_size_inp = int(input("Enter the size of list : "))

for i in range(list_size_inp):
    user_input = int(input(f"Enter {i+1} number : "))
    list.append(user_input)

for i in list:
    count = 0
    for j in range(len(list)):
        if i == list[j]:
            count += 1
    dict.update({str(i): count})

print(dict)

# print the number(key) which repeated most times
for key, value in dict.items():
    if value == max(dict.values()):
        print(f"\nMost repeated number is {key} and it repeated {max(dict.values())} times ")


