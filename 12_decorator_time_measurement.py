import asyncio
import time

def async_timed(f):

    async def wrapper():
        start = time.time()
        result = await f()
        end = time.time()
        print(f"Time: {end - start}")
        return result
     
    return wrapper


@async_timed
async def coro1():
    await asyncio.sleep(2)
    return 100


async def main():
    result = await coro1()
    print(result)

asyncio.run(main())