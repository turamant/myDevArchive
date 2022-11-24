from abc import ABCMeta, abstractmethod


class Product:
    def __init__(self):
        self.data: str = ""

    def about(self) -> str:
        return self.data

    def append_data(self, string:str):
        self.data += string


class Car(Product):
    def __init__(self):
        super().__init__()


class Manual(Product):
    def __init__(self):
        super().__init__()


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def setSeats(self):
        pass

    @abstractmethod
    def setEngine(self):
        pass

    @abstractmethod
    def setTripComputer(self):
        pass

    @abstractmethod
    def setGPS(self):
        pass

    @abstractmethod
    def getResult(self):
        pass


class CarBuilder(Builder):
    def __init__(self) -> None:
        self.__car = Car()

    def reset(self):
        """Поместить новый объект Car в поле 'car'."""
        self.__car.append_data("Произведен автомобиль Тойота\n")

    def setSeats(self):
        """Установить указанное количество сидений."""
        self.__car.append_data("Установлено 4 сиденья\n")

    def setEngine(self):
        """Установить поданный двигатель."""
        self.__car.append_data("Установлен двигатель ТурбоСпорт\n")

    def setTripComputer(self):
        """Установить поданную систему навигации."""
        self.__car.append_data("Установлен бортовой компьютер логик\n")

    def setGPS(self):
        """Установить или снять GPS."""
        self.__car.append_data("Установленнн GPS навигатор\n")

    def getResult(self) -> Car:
        """Вернуть текущий объект автомобиля."""
        return self.__car


class CarManualBuilder(Builder):
    def __init__(self) -> None:
        self.__manual = Manual()

    def reset(self):
        """Поместить новый объект Car в поле 'car'."""
        self.__manual.append_data("Произведено руководство автомобиль Тойота\n")

    def setSeats(self):
        """Установить указанное количество сидений."""
        self.__manual.append_data("Описание об установке 4 сидений\n")

    def setEngine(self):
        """Установить поданный двигатель."""
        self.__manual.append_data("Глава описания двигателя ТурбоСпорт\n")

    def setTripComputer(self):
        """Установить поданную систему навигации."""
        self.__manual.append_data("Глава бортовой компьютер логик\n")

    def setGPS(self):
        """Установить или снять GPS."""
        self.__manual.append_data("Глава GPS навигатор\n")

    def getResult(self) -> Manual:
        """Вернуть текущий объект автомобиля."""
        return self.__manual


class Director:
    def __init__(self, builder: Builder):
        self.__builder = builder

    def set_builder(self, builder: Builder):
        self.__builder = builder

    def mount_simple_car(self) -> Product:
        self.__builder.reset()
        self.__builder.setEngine()
        self.__builder.setSeats()
        return self.__builder.getResult()

    def mount_best_car(self) -> Product:
        self.__builder.reset()
        self.__builder.setEngine()
        self.__builder.setSeats()
        self.__builder.setGPS()
        self.__builder.setTripComputer()
        return self.__builder.getResult()


if __name__ == '__main__':
    car_builder: Builder = CarBuilder()
    director = Director(car_builder)
    toyota: Product = director.mount_simple_car()
    print(toyota.about())

    manual_builder: Builder = CarManualBuilder()
    director = Director(manual_builder)
    manual_toyota: Product = director.mount_best_car()
    print(manual_toyota.about())



