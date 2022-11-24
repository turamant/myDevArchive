from typing import Generator
import time


def fibo_generator(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1

    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next
        yield next


if __name__ == '__main__':
    start = time.time()
    for i in fibo_generator(121):
        print(i)

    end = time.time()
    print(f'Threads took {end - start:.4f} seconds.')


