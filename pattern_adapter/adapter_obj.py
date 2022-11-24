from abc import ABCMeta, abstractmethod


class IScale(metaclass=ABCMeta):
    @abstractmethod
    def get_weight(self) -> float:
        pass


class BritishScale(IScale):
    def __init__(self, cw: float):
        self.__current_weight = cw

    def get_weight(self) -> float:
        return self.__current_weight


class RussianScale(IScale):
    def __init__(self, cw: float):
        self.__current_weight = cw

    def get_weight(self) -> float:
        return self.__current_weight


class AdapterBritishScale(IScale):
    def __init__(self, british_scale: BritishScale):
        self.__british_scale = british_scale

    def get_weight(self) -> float:
        return self.__british_scale.get_weight() * .453591


class AdapterRussianScale(IScale):
    def __init__(self, russian_scale: RussianScale):
        self.__russian_scale = russian_scale

    def get_weight(self) -> float:
        return self.__russian_scale.get_weight() *2.2046


if __name__ == '__main__':
    kg: float = 55. # кг
    lb: float = 55. # Фунты

    ruScales = RussianScale(kg)
    brScales = AdapterBritishScale(BritishScale(lb))

    print(ruScales.get_weight(), "кг")
    print(brScales.get_weight(), "кг")

    print("#" * 28)

    br = BritishScale(24) # фунтов
    ru = AdapterBritishScale(br)
    print(br.get_weight(),"фунт", "->", ru.get_weight(),"кг")

    ru2 = RussianScale(24) # кг
    br2 = AdapterRussianScale(ru2)
    print(ru2.get_weight(), "кг", "->", br2.get_weight(), "фунт")