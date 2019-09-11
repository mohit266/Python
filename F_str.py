import math

# String formatting

me = "Mohit"
a = 21
'''
b = "This is %s"%me
print(b)

# c = "Age of %s is %s"%(me, a)
# print(c)
d = "This is {0} and age of {0} is {1}"
#            0,  1
c = d.format(me, a)
print(c)

'''
# F string
var = f"This is {me} {a} {math.cos(60)}"
print(var)

