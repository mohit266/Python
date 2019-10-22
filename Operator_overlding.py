# https://docs.python.org/3/library/operator.html
# Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name.
# Dunder here means “Double Under (Underscores)”.
# These are commonly used for operator overloading.
# Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        return f"\n Name of employee {self.name}" \
               f"Age is {self.age}"

#   Operator overloading
    def __add__(self, other):
        return self.age + other.age

    def __truediv__(self, other):
        return self.age / other.age

A1 = Employee("Mohit", 30)
A2 = Employee("Rahul", 5)

print(A1+A2)
print(A1/A2)