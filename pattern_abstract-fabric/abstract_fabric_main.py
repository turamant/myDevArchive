from abc import ABCMeta, abstractmethod


class IEngine(metaclass=ABCMeta):
    @abstractmethod
    def release_engine(self):
        pass


class JapanEngine(IEngine):
    def release_engine(self):
        print("Выпустили японский двигатель")


class DeutschEngine(IEngine):
    def release_engine(self):
        print("Выпустили немецкий двигатель")


class ICar(metaclass=ABCMeta):
    @abstractmethod
    def release_car(self, engine: IEngine):
        pass


class JapanCar(ICar):
    def release_car(self, engine: IEngine):
        print("Сделали японский автомобиль")
        engine.release_engine()


class DeutschCar(ICar):
    def release_car(self, engine: IEngine):
        print("Сделали немецкий автомобиль")
        engine.release_engine()


class IFabric(metaclass=ABCMeta):
    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def create_car(self):
        pass


class JapanFabric(IFabric):
    def create_engine(self):
        return JapanEngine()

    def create_car(self):
        return JapanCar()


class DeutschFabric(IFabric):
    def create_engine(self):
        return DeutschEngine()

    def create_car(self):
        return DeutschCar()


if __name__ == '__main__':
    j_factory = JapanFabric()
    j_engine = j_factory.create_engine()
    j_car = j_factory.create_car()

    j_car.release_car(j_engine)

    d_factory = DeutschFabric()
    d_engine = DeutschEngine()
    d_car = DeutschCar()

    d_car.release_car(j_engine)




