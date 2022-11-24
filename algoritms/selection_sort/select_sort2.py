score = [155, 203, 99, 201, 12, 89]


def find_small_index(arr: list):
    smallest = arr[0]
    small_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            small_index = i
    return small_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_small_index(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort(score))