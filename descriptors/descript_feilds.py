from decimal import Decimal


class Fields:
    def __init__(self, name):
        self.name = name
        self.internal_name = '__' + self.name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Person:
    first_name = Fields('first_name')
    last_family = Fields('last_name')
    prefix = Fields('prefix')
    suffix = Fields('suffix')
    rate = Decimal('0.5')
    second = Decimal('5')




person = Person()
print('До: ', repr(person.first_name), person.__dict__)


person.first_name = 'Evclid'
print('После: ', repr(person.first_name), person.__dict__)



cost = (person.rate * person.second / Decimal('6')) / Decimal('2') * 1000000
print("точность: ", cost)

