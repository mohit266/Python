import time
from functools import lru_cache


@lru_cache(maxsize=3)
def some_work(n):
    fr_st = int(input("Enter first number : "))
    sc_nd = int(input("Enter second number : "))
    print("Displaying the result")
    time.sleep(n)
    print("Enter any key to show the addition of two number")
    input()
    print(fr_st+sc_nd)

if __name__ == '__main__':
    some_work(3)
