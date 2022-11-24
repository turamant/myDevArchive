from abc import ABC, abstractmethod


class Logistic(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self) -> str:
        transport = self.create_transport()
        result = f'Создали {transport.deliver()}'
        return result


class RoadLogistics(Logistic):
    def create_transport(self):
        return Track()


class SeaLogistics(Logistic):
    def create_transport(self):
        return Ship()


class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Track(Transport):
    def deliver(self):
        print("Доставка по суше")


class Ship(Transport):
    def deliver(self):
        print("Доставка по морю")


class Product:
    def __init__(self, name, count):
        self.name = name
        self.count = count


if __name__ == '__main__':
    creator = RoadLogistics()
    creator.plan_delivery()
    truck = creator.create_transport()
    print("Truck", id(truck))

    creator = SeaLogistics()
    creator.plan_delivery()
    ship = creator.create_transport()
    print("Ship", id(ship))

    product = Product("car", 5)
    print(product.name, product.count)

