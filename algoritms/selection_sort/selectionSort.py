import time
from random import randint

# Время O(n2) работает медленне из-за передвижения индексов в списике!!!


def selection_sort(arr: list) -> None:
    for i in range(len(arr)):
        lowest_element_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_element_index]:
                lowest_element_index = j
        arr[i], arr[lowest_element_index] = arr[lowest_element_index], arr[i]


random_list_of_nums = [randint(1, 100) for x in range(10000)]
print("Before sort: ", random_list_of_nums)
start = time.time()
selection_sort(random_list_of_nums)
timer = time.time() - start
print(f"Время сортировки: {timer:.2f}")
print("After sort: ", random_list_of_nums)



def find_small_index(arr: list):
    smallest = arr[0]
    small_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            small_index = i
    return small_index


# Работает быстрее засчет записи в новый список !!! # Время так же O(n2)
def select_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_small_index(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


random_list = [randint(1, 100) for y in range(10000)]
start2 = time.time()
n_arr = select_sort(random_list)
timer2 = time.time() - start2
print(f"Время сортировки: {timer2:.2f}")
print("After sort: ", n_arr)


