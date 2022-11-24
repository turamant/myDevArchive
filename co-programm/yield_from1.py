def fun_gen1():
    yield 1
    yield 2
    return "Это типа вернула сопрограмма await"


def fun_gen2():
    yield 3
    result = yield from fun_gen1()  # await!
    print("-->", result)
    yield 4

for i in fun_gen2():
    print(i)
