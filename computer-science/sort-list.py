'''
Есть два отсортированных по алфавиту списка, нужно сделать объединение этих списков,
то есть создать новый третий список с отсортированными поалфавиту данными
'''


def union_two_list(car: list, moto: list):
    count = 0
    while len(car) != 0 and len(moto) != 0:
        if car[count] < moto[count]:
            new_list.append(car[count])
            car.pop(car[count])

        else:
            new_list.append(moto[count])
            moto.pop(moto[count])
        count += 1




if __name__ == '__main__':
    new_list = list()
    car = [1,3,5,7,9,1,2,3,4,6]
    moto = [1,2,5,8,9,5,65,7,8,9]
    union_two_list(car, moto)
    print("...", new_list)


