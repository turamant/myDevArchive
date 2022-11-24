import random


class Person:

    def __init__(self, name='xxx', age=1):
        self.name = name
        self.age = age

    def create_new_person(self):
        self.age = random.randint(18, 85)
        self.name = self.random_name()
        return f'{self.name}: {self.age}'

    @staticmethod
    def random_name() -> str:
        name = list()
        for c in range(10):
            name.append(chr(random.randint(98, 122)))
        return "".join(name)

    def __call__(self, *args, **kwargs):
        return self.create_new_person()


if __name__ == '__main__':
    person_list = list()
    person = Person()
    print(callable(person))
    for i in range(10):
        print(person(), id(person()))
        person_list.append(person())
    print(" == "* 28)
    for i in person_list:
        print(i, ":", id(i))
