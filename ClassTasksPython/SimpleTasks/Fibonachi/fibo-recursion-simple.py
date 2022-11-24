import time


def fibo(n: int) -> int:
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


fibo_list = list()


if __name__ == '__main__':
    start = time.time()
    for i in range(0, 21):
        fibo_list.append(fibo(i))

    print(*fibo_list)
    end = time.time()
    print(f'Threads took {end - start:.4f} seconds.')
