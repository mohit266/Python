from datetime import datetime


def f_age():
    birth_year = int(input("Enter your birth year to know your age :"))
    current_year = datetime.now().year

    if birth_year < current_year:
        select_year = int(input("Enter any year to know your age in particular year:"))
        remaining_yr = select_year - current_year
        current_age = current_year - birth_year
        future_age = current_age + remaining_yr
        find_year = 100 - current_age
        turn_100 = current_year + find_year
        print(f"You are {current_age} year old ")
        print(f"Your age in year {select_year} will be:{future_age}")
        print(f"You will turn 100 in year {turn_100}")

    elif birth_year > current_year:
        print("You are not yet born ")

    else:
        print("Please enter birth year in 19's or 20's")

if __name__ == '__main__':
    f_age()
