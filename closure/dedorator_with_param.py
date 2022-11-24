import time


def param(active=True):
    def decor(func):
        def closure(*args):
            if active:
                start = time.time()
                res = f'Старт: {start:.2f}' + f'Res: {str(func(*args))}' + f'Время: {start - time.time():.20f}'
            else:
                res = func(*args)
            return res
        return closure
    return decor


@param(active=True)
def add(x, y):
    return x ** y


@param(active=False)
def mut(x, y):
    return x * y


print(add(9, 18))
print(mut(2, 34))
