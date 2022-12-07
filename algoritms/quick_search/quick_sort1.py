import time
from random import randint

# очень быстрая сортировка  O(n log n)
# менее 0.1 секунды


def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        grate = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(grate)


random_list: list = [randint(1, 100) for x in range(1, 10000)]
start = time.time()
new: list = quick_sort(random_list)
end = time.time() - start

#print("Before sort: ", random_list)
#print("After sort: ", new)
print(f"Скорость: {end:.2f}")

random_list2: list = [randint(1, 100) for y in range(1, 10000)]
start2 = time.time()
new2: list = sorted(random_list2)
end2 = time.time() - start2

#print("Before sort2: ", random_list2)
#print("After sort2: ", new2)
print(f"Скорость2 : {end2:.2f}")