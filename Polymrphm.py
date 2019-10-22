class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        return f"\nName of person is {self.name} \n" \
               f"Age is {self.age} "


class Employee(Person):
    def __init__(self, name, age, company_name):
        super().__init__(name, age)
        self.company_name = company_name

    def print_details(self):
        print(super().print_details())
        return f"He works in {self.company_name} company "


class Programmer(Employee):
    def __init__(self, name, age, company_name, language):
        super().__init__(name, age, company_name)
        self.language = language

    def print_Details(self):
        print(super().print_details())
        return f"He knows {self.language} language \n"

david = Employee("MS", 25, "Cricket")
print(david.print_details())

Mohit = Programmer("Mohit", 21, "Metacube", "Python")
print(Mohit.print_Details())

