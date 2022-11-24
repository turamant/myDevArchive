

COEFFICIENT: float = 3.281


def wrapperF(func):
    def inner(*args, **kwargs) -> float:
        opt: int = func(*args, **kwargs)
        res: float = opt * COEFFICIENT
        print("Значение площади в футах: ", res)
        return res
    return inner


@wrapperF
def square(x, y):
    return x * y


if __name__ == '__main__':
    print("Введите значения в метрах")
    square: float = square(2, 5)
