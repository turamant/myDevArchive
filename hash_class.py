def power(x: int, y: int) -> int:
    return x * y


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'{self.x}, {self.y}'

    def __repr__(self) -> str:
        return "Point({0.x!r}, {0.y!r})".format(self)


class Circle(Point):
    def __init__(self, radius: int, x: int = 0, y: int = 0):
        super(Circle, self).__init__(x, y)
        self.radius = radius

    def __str__(self) -> str:
        return f'{self.x}, {self.y}, {self.radius}'


p = Point(12, 14)

c = Circle(3, 5, 6)

print(c)
