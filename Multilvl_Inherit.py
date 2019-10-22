class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        return f"Name of person is {self.name} \n" \
               f"Age is {self.age} \n"


class Employee(Person):
    def __init__(self, name, age, company_name):
        self.name = name
        self.age = age
        self.company_name = company_name

    def print_details(self):
        return f"Name of employee is {self.name} \n" \
               f"Age is {self.age} \n" \
               f"He works in {self.company_name} company \n"


class Programmer(Employee):
    def __init__(self, name, age, company_name, language):
        self.name = name
        self.age = age
        self.company_name = company_name
        self.language = language

    def print_Details(self):
        return f"Name of employee is {self.name} \n" \
               f"Age is {self.age} \n" \
               f"He works in {self.company_name} company \n" \
               f"He knows {self.language} lamguage \n"

Mohit = Programmer("Mohit", "21", "Metacube", "Python")
print(Mohit.print_Details())

Rahul = Person("Rahul", 20)
print(Rahul.print_details())

Jai = Employee("Jai", 21, "Liontrol")
print(Jai.print_details())