import asyncio
from util import delay

async def add_one(n: int) -> int:
    return n + 1

async def hello_there_coro() -> str:
    await delay(1)
    return 'hello world!'

async def main():
    message = await hello_there_coro()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)


asyncio.run(main())

