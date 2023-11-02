import asyncio
from util import async_timed

@async_timed()
async def delay(n: int) -> int:
    print(f"Sleeping for {n} seconds.")
    await asyncio.sleep(n)
    print(f"Finished sleeping.")
    return n

async def main():
    coro1 = asyncio.create_task(delay(3))
    result = await coro1
    print("result: %s" % (result))


asyncio.run(main())