# user defined functions

def function1(a,b):
    # This is doc string
    """ This is a function which will calculate average of two numbers """
    average = (a+b)/2
    return average

v = (function1(2,4))
print(v)

# To print doc string
print(function1.__doc__)
