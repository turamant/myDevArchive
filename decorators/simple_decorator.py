def info_print(func):
    def wrapper(*args):
        result = func(*args)
        return 'Hello :' + str(result) + ' world'
    return wrapper


@info_print
def power(x, y):
    return x * y


if __name__ == '__main__':
    r = power(2, 3)
    print(r)
