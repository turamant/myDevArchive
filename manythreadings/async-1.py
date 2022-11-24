import asyncio
import time

from util import delay


async def add_one(number: int) -> int:
    await delay(3)
    return number + 1


async def messages() ->None:
    for i in range(2):
        await asyncio.sleep(1)
        print('Hello world!')


async def main() -> None:
    result_1 = asyncio.create_task(add_one(1))
    result_2 = asyncio.create_task(add_one(2))
    result_3 = asyncio.create_task(add_one(3))
    result_4 = asyncio.create_task(add_one(4))
    await messages()
    await result_1
    await result_2
    await result_3
    await result_4


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Время работы: {end - start:.4f} с.")


