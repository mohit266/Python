class Emp:

    no_of_leaves = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_det(self):
        return f"The name of employee is {self.name} and age of employee is {self.age}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))


class Prg(Emp):

    def __init__(self, name, age, languages):
        self.name = name      # We can also use super keyword
        self.age = age
        self.languages = languages

    def print_prg(self):
        return f"The Programmer's name is {self.name} and age of employee is {self.age} and languages are {self.languages}"

rahul = Emp("Rahul", 20)
print(rahul.print_det())

mohit = Prg("Mohit", 21, ["Python"])
print(mohit.print_prg())

david = Prg("David", 25, ["Java"])
print(david.print_prg())