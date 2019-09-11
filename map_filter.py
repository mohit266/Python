# ------------------- MAP------------------
num = ["4", "8" ,"10" , "15", "20"]

# for i in range(len(num)):
#    num[i] = int(num[i])

# num[2] = num[2] + 1
# print(num[2])

a = list(map(int, num))
a[2] = a[1] + 1
print(a[2])

# b = list(map(lambda x: x*x, num))
# print(b)

def square(x):
    return x*x

def cube(x):
    return x*x*x

func = [square, cube]

for i in num:
    c = list(map(lambda x:x(i), func))
    print(c)

# ------------------FILTER----------------
list1 =[3, 6, 8, 1, 10, 15, 4]

def is_greater_5(num):
    return num>5

gr_than = list(filter(is_greater_5, list1))
print(gr_than)

# -------------------REDUCE-----------------
from functools import reduce
list2 =[3, 6, 8, 1, 10, 15, 4]
num1 = reduce(lambda x,y:x+y, list2)
print(num1)
