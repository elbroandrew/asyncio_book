import functools
import time
from typing import Callable, Any
import asyncio


def async_timed():
    def wrapper(f: Callable) -> Callable:

        @functools.wraps(f)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"Staring func {f.__name__} with args: {args}, {kwargs}")
            start = time.time()
            try:
                return await f(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"Total time: {total} seconds.")

        return wrapped
    
    return wrapper

            


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