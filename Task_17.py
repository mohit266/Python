# Convert list into string.
n_str = ""
list = []
usr_input = int(input("Enter the size of list:"))
for i in range(usr_input):
    element_input = int(input(f"Enter {i+1} number:"))
    list.append(element_input)
print(list)
for i in list:
    n_str += str(i)

print(n_str)