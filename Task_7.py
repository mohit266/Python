def next_palindrome(n):
    while not is_palindrome(n):
        n = n+1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    usr_input = int(input("Enter number of test cases: "))
    number = []

    for i in range(usr_input):
        num = int(input(f"Enter the {i+1} number : "))
        number.append(num)
    # print(number)

    for i in range(usr_input):
        print(f"The next palindrome for {number[i]} is {next_palindrome(number[i])}")