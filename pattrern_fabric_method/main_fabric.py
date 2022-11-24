from enum import Enum
import math


class Coordinate(Enum):
    POLAR = 0
    CARTESIAN = 1


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x:{self.x}, y:{self.y}'

    @staticmethod
    def make_point__polar(x, y):
        return Point(x, y)

    @staticmethod
    def make_point_cartesian(ro, theta):
        return Point(ro*math.sin(theta), theta*math.cos(ro))

    @classmethod
    def make_point_cls(cls):
        return cls(3, 2)


def make_point__polar(x, y):
    return Point(x, y)


if __name__ == '__main__':
    p = Point(1, 2)
    print(p)
    print('*' * 28)
    polar = Point.make_point__polar(1, 2)
    print(polar)
    print('*' * 28)
    cartesian = Point.make_point_cartesian(1, 2)
    print(cartesian)
    print("#" * 28)
    obj = make_point__polar(6, 7)
    print(obj)
    print("#" * 28)
    new_cls_point = Point.make_point_cls()
    print("......", new_cls_point)
