# Basic rules of python
'''
print("Hello Mohit!!", end=" ")
print("How are You")

# Escape function
print("C:\\nohit")

# variable
var1 = "Python"
var2 = 10
var3 = 30

# Typecasting
print(var1+str(var3))

# Addition of two numbers
#a = int(input("Enter first number :"))
#b = int(input("Enter Second number :"))
#print("Addition of two numbers is : ", a+b)

# string slicing
mystr = "Enjoy your life"
print(mystr)
#print(len(mystr))
#print(mystr[0:5:2])
#print(mystr.capitalize())
#print(mystr.upper())
#print(mystr.casefold())
#print(mystr.endswith("life"))
print(mystr.split("5"))

# list slicing

number = [2,6,1,40,25]
print(number)

# insert function add the value on a particular index
number.insert(2,57)
print(number)

# pop remove the last element in the list
number.pop()
print(number)

# append
number.append(86)
print(number)

# (list) Mutable --> Can Change
# (tuple) Immutable --> Cannot Change

# Tuple
tp = (1,3,7)
# tp[1]=8 We cannot change the value of tuple
print(tp)

z = tuple(mystr)
print(z)

# Dictionary
dict = {"Meena":"Toffee","Jai":"Food","Mohit":"Coffee","Maan":"Burger"}
print(dict)

dict.update({"Rahul":"Pizza"})
print(dict)

del dict["Rahul"]
print(dict.keys())
'''

D = {"Food":"Burger","List":"Mutable","Tuple":"Immutable","Maan":"Body_Builder"}
print("Enter any  word ",
      "\n 1.Food",
      "\n 2.List",
      "\n 3.Tuple",
      "\n 4.Maan")
result = D[input("Enter any word : ")]
print("Meaning :", result)