def pallndrme(n):
    if n//10 == 0:
        return False

    temp = n
    rev_num = 0

    while temp != 0:
        rev_num = rev_num * 10 + temp % 10
        temp = temp//10

    if rev_num == n:
        yield rev_num

    else:
        print("Number is not palindrome")
        exit()

if __name__ == '__main__':
    num = int(input("Enter a number to check palindrome or not: "))
    x = pallndrme(num)
    print("Number is palindrome : ", x.__next__())