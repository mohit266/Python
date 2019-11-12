def next_palindrme(n):
    while not is_palindrme(n):
        n += 1
    return n


def is_palindrme(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    list = []
    new_list = []
    list_size = int(input("Enter the size of the list:"))
    for i in range(list_size):
        # Enter list element one by one
        user_input = int(input(f"Enter {i+1} number : "))
        list.append(user_input)
    print(f"Your entered list is {list}")
    for i in list:
        if i > 10:
            val = next_palindrme(i)
            # print(f"the next palindrome of {i} is {val}.")
            new_list.append(val)
        else:
            new_list.append(i)
    print(f"The list of next palindrome is {new_list}")