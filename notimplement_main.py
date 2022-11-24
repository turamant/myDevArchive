class Car:
    def drive(self):
        raise NotImplemented


class Volvo(Car):
    def drive(self):
        return f"tutu"


if __name__ == '__main__':
    volvo = Volvo()
    print(volvo.drive())
