# Basic concepts of oop
class Student:
    no_of_leaves = 5
    pass

# create an object of Student class
Mohit = Student()
Rahul = Student()

Mohit.name = "Mohit"
Mohit.std = "B.tech"
Mohit.section = 1

Rahul.name = "Rahul"
Rahul.std = "B.com"
Rahul.section = 2

print(Mohit.name, Rahul.section)
print(Mohit.no_of_leaves)

# only class itself change its variable value
Student.no_of_leaves = 6
print(Student.no_of_leaves)

# instance of class cannot change the variable of class
Rahul.no_of_leaves = 7
print(Student.no_of_leaves)