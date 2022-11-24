from math import log2, sqrt

data: int = 4000000000
print("1: ", log2(data))

i: int = 0
s: int = 0
index_list1: list = list()

while s < data:
    s = 2 ** i
    index_list1.append(i)
    i += 1
print("2: ", max(index_list1))


index_list2: list = list()
for i in range(100):
    s = 2 ** i
    if s <= data:
        index_list2.append(i)
print("3: ", max(index_list2))





