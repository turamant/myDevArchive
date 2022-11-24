from array import array


class Byte:
    __slots__ = '__x, __y'

    pass

class Vector2d:
    typecode = 'd'
    __slots__ = ('__x', '__y')

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __str__(self):
        return f'Vector2d{self.__x, self.__y}'

    def __hash__(self):
        return hash(self.__x)


    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    '''def __iter__(self):
        return (i for i in (self.x, self.y))

    def generator(self):
        for i in (self.x, self.y):
            yield i

    def __bytes__(self):
        c = bytes([ord(self.typecode)]) + (bytes(array(self.typecode, self)))
        return c

    @classmethod
    def alt_constructor(cls):
        return cls(10, 20)'''


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3, 4)
    print(v1.x, v1.y)
    print(v1)
    #x, y = v1  # итератор
    #print(x, y)
    #gen = v1.generator()
    #print("..",next(gen))
    #print("..", next(gen))
    #n = Vector2d.alt_constructor()
    #print(n.x, n.y)
    #print(hash(n))
    print(hash(v1.x))

    print(v1.x)

    d = {v1.x: "stroka1", v1.y: "second"}
    for k, v in d.items():
        print(k, ":", v)

    if (v1.x, v1.y) == (v2.x, v2.y):
        print("YEs")
    else:
        print("no")

