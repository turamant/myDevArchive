from math import log2

data: int = 128
print("1: ", log2(data))

i: int = 0
s: int = 0
index_list: list = list()

while s < data:
    s = 2 ** i
    index_list.append(i)
    i += 1
print("2: ", max(index_list))

for i in range(data):
    s = 2 ** i
    if s <= data:
        index_list.append(i)
print("3: ", max(index_list))



