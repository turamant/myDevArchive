
class IncorrectBill:
    def __init__(self):
        cost_by_dish = []
        self.cost_by_dish = cost_by_dish


one = IncorrectBill()
two = IncorrectBill()

one.cost_by_dish.append(1)
two.cost_by_dish.append(2)

print(one.cost_by_dish)
print(two.cost_by_dish)

print(one.cost_by_dish is two.cost_by_dish)

print('#' * 28)


class IncorrectBill2:
    cost_by_dish = []

    def __init__(self):
        self.cost_by_dish = IncorrectBill2.cost_by_dish


one = IncorrectBill2()
two = IncorrectBill2()

one.cost_by_dish.append(1)
two.cost_by_dish.append(2)

print(one.cost_by_dish)
print(two.cost_by_dish)

print(one.cost_by_dish is two.cost_by_dish)


print("*" * 28)


class IncorrectBill3:
    def __init__(self, cost_by_dish=[]):
        self.cost_by_dish = cost_by_dish


one = IncorrectBill3()
two = IncorrectBill3()

one.cost_by_dish.append(1)
two.cost_by_dish.append(2)

print(one.cost_by_dish)
print(two.cost_by_dish)

print(one.cost_by_dish is two.cost_by_dish)
