# capitalize the first letter of string.
ls = []
n_str = input("Enter any name :")
li_st = n_str.split(' ')
# print(li_st)
for i in li_st:
    ls.append(f"{i[0].upper()}{i[1:]}")
for i in ls:
    print("".join(i), end=" ")
