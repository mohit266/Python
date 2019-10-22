from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def print_area(self):
        area = self.length * self.breadth
        print("Area of rectangle is", area)

rect = Rectangle(5, 6)
rect.print_area()