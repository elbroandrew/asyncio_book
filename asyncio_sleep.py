import asyncio
from util import delay

async def add_one(n: int) -> int:
    await delay(2)
    return n + 1

async def hello_there_coro() -> str:
    await delay(1)  # await puts everyithing on pause
    return 'hello world!'

async def main():
    message = await hello_there_coro()
    print("some message.") # this will happen after we 'awaited' the result from 'hello_there' func.
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)


asyncio.run(main())

