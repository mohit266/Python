def count_string(str):
    count = 0
    user_input = input("Enter the string you want to count : ")
    for i in range(len(str)-1):
        count += str[i:i+len(user_input)] == user_input.capitalize()
    return count


if __name__ == '__main__':
    count = count_string("Mohit is good developer. Mohit is aslo a writer")
    print(f"Mohit appeared {count} times")