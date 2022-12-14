my_list = [1, 2, 3, 444, 9, 6, 5, 12, 65, 13, 8, 23]

l = []


def summ(arr: list) -> int:
    total = 0
    for x in arr:
        total += x
    return total


print("Summ_list: ", summ(my_list))


def summ_recurs(arr: list) -> int:
    if len(arr) == 0:
        return 0
    return arr[0] + summ_recurs(arr[1:])


print("recursion_summ: ", summ_recurs(my_list))


def factorial(n: int) -> int:
    if n == 1:
        return n
    return n * factorial(n - 1)


print("Factorial: ", factorial(7))


"""
recursion counter len(list) 
"""


def count_elements_in_list(arr: list) -> int:
    count = 0
    for _ in arr:
        count += 1
    return count


print(" Простой способ: ",count_elements_in_list(my_list))
print(count_elements_in_list(l))


def count_recursion(arr: list) -> int:
    if not arr:
        return 0
    return 1 + count_elements_in_list(arr[1:])


print("Рекурсивный подсчет элементов: ", count_elements_in_list(my_list))
print(count_elements_in_list(l))


def max_element_in_list(arr: list) -> int:
    maximum = 0
    for i in arr:
        if i > maximum:
            maximum = i
    return maximum


print("Max element from list: ", max_element_in_list(my_list))


def max_recursion(arr: list) -> int:
    if len(arr) == 1:
        return arr[0]
    m = max_recursion(arr[1:])
    return m if m > arr[0] else arr[0]


print("Max recursion: ", max_recursion(my_list))