
class Person:
    __shared_attrs = {
        'name': 'ivan',
        'age': 21
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


p1 = Person()
p2 = Person()
print(id(p1), id(p2))
p1.name = "Kozel"
print(p1.name)
print(p2.name)

