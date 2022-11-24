class Averager:
    def __init__(self):
        self.value_list = list()

    def __call__(self, value):
        self.value_list.append(value)
        avg = sum(self.value_list) / len(self.value_list)
        return avg


def make_avarage():
    value_list = list()

    def averager(value):
        value_list.append(value)
        avg = sum(value_list) / len(value_list)
        return avg
    return averager


def make_average2():
    count = 0
    value = 0

    def averager(new_value):
        nonlocal count, value
        count += 1
        value += new_value
        return value / count
    return averager


m2 = make_average2()
m2(10)
m2(11)
print("быстро работает: ", m2(15))



m = make_avarage()
m(10)
m(11)
print("++ ",m(15))







avg = Averager()
avg(1)
avg(2)
avg(3)
print(avg(4))
