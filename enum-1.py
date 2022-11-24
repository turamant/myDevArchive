from enum import Enum


class Color(Enum):
    red = 1
    blue = 2
    green = 3


class Car:
    def __init__(self, name):
        self.name = name
        self.color = Color


mycar = Car('toyota')
print(mycar.color.green)

