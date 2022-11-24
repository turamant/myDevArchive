import time

memo: dict = {0: 0, 1: 1}


def fibo(n: int) -> int:
    if n not in memo:
        memo[n]: int = fibo(n - 1) + fibo(n - 2)
    return memo[n]


fibo_list: list = list()


if __name__ == '__main__':
    start = time.time()
    for i in range(0, 21):
        fibo_list.append(fibo(i))

    print(*fibo_list)
    end = time.time()
    print(f'Threads took {end - start:.4f} seconds.')

