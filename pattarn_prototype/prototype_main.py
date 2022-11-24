import copy
import random
import string


class Sheep:
    __name = ""
    __params = {"Вес": 20, "Рост": 34}

    def __init__(self, donor: 'Sheep' = None):
        if donor:
            self.__name: str = donor.get_name()
            self.__params: dict = copy.deepcopy(donor.get_params())

    def set_name(self, newname) -> None:
        self.__name: str = newname

    def get_name(self) -> str:
        return self.__name

    def set_weight(self, weight: int, rost: int) -> None:
        self.__params["Вес"]: int = weight
        self.__params["Рост"]: int = rost

    def get_params(self) -> dict:
        return self.__params

    def clone(self) -> 'Sheep':
        return Sheep(self)


class Clone:
    list_clone: list = list()

    def generator_clone(self, number) -> list:
        for i in range(number):
            clone: Sheep = donor.clone()
            clone.set_weight(random.randint(20, 50), random.randint(28, 36))
            clone.set_name("".join(random.choices(string.ascii_uppercase + string.digits, k=6)))
            self.list_clone.append(clone)
        return self.list_clone

    def display_clone(self):
        count_clone: int = 0
        for clone in self.list_clone:
            count_clone += 1
            print(count_clone, " : ", id(clone), "Имя овцы: ", clone.get_name(), clone.get_params())

    def stupid_count(self):
        stupid_count: int = 0
        for select in self.list_clone:
            if select.get_params() == {"Вес": 42, "Рост": 28}:
                select.set_name("Тупая овца")
                print(id(select), "Имя овцы: ", select.get_name(), select.get_params())
                stupid_count += 1
        print("Тупых овец :", stupid_count)


if __name__ == '__main__':
    clone: Clone = Clone()

    donor: Sheep = Sheep()
    donor.set_name("Долли")

    clone.generator_clone(1000)

    clone.display_clone()
    print(" # " * 29 )
    clone.stupid_count()

