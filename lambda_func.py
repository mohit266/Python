# lambda functions and anonymous functions

# def minus(x,y):
#     return x-y

# minus = lambda x, y: x-y
# print(minus(9, 4))

a = [[2, 5], [7, 1], [2,15]]

# key takes function as input , nd lambda is a one line function
a.sort(key= lambda x: x[1])
print(a)