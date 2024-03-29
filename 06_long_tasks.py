import asyncio
from util import delay


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print(f"I am running other code, while I am waiting!")


async def main():
    delay1 = asyncio.create_task(delay(3))
    delay2 = asyncio.create_task(delay(3))
    await hello_every_second()
    await delay1
    await delay2

asyncio.run(main())