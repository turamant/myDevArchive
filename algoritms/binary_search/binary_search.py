import random


def search_binary(hidden_number: int, array: list) -> None:
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = round((low+high) / 2)
        guess = array[mid]
        print("..",guess)
        if guess == hidden_number:
            return array[mid]
        if array[mid] > hidden_number:
            high = mid - 1
        else:
            low = mid + 1

    return None


print("Игра отгадай число от 1- до 100")
array = sorted([random.randint(1, 100) for x in range(1, 10)])
print("Наш список: ", array)
hidden_number = random.choice(array)
print("Было загадано: ", hidden_number)
print(" Мы отгадали: ",search_binary(hidden_number, array))





