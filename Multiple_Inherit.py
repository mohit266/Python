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


class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def print_details(self):
        return f"The name of player is {self.name} and game is {self.game}"


class Prg(Emp, Player):

    languages = "C++"

    def print_language(self):
        print(self.languages)


rahul = Prg("Mohit", "21")
print(rahul.print_det())
rahul.print_language()

