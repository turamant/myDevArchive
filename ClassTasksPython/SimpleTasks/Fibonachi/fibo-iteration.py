import time


def fibo_iteration(n: int) -> int:
    if n == 0:
        return n

    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next

    return next


fibo_list: list = list()


if __name__ == '__main__':
    start = time.time()
    for i in range(0, 121):
        fibo_list.append(fibo_iteration(i))

    print(*fibo_list)
    end = time.time()
    print(f'Threads took {end - start:.4f} seconds.')


