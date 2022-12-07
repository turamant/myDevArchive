import asyncio


async def add_one(n: int) -> int:
    await asyncio.sleep(3)
    return n + 1


def my_func(n: int) -> int:
    return n + 1


async def main(n):
    if n > 0:
        return await add_one(n)
    else:
        return await add_one(n)


coroutine = asyncio.run(add_one(1))
result = my_func(1)
mainer = asyncio.run(main(-6))

if __name__ == '__main__':
    print(coroutine, ' : ', type(coroutine))
    print(result, ' : ', type(result))
    print(mainer, '=', type(mainer))

