class Car:
    def __init__(self, title, color):
        self.__title = title
        self.color = color

    @property
    def title(self):
        return self.__title


class Audi(Car):
    def __init__(self):
        super().__init__(title='Audi', color='white')


car = Car("Moskvich", 'blue')
print(car.title, car.color)
audi = Audi()
print(audi.title, audi.color)