from asyncio import Future
import asyncio


"""
Futures can also be used in await expressions. If we await a future , we’re saying
“pause until the future has a value set that I can work with, and once I have a value,
wake up and let me process it.”
If you have used
JavaScript in the past, this concept is analogous to 'promises'. In the Java world, these are
known as 'completable futures'.
"""

def make_request() -> Future:
    future1 = Future()
    asyncio.create_task(run_future(future1))
    return future1


async def run_future(future: Future):
    await asyncio.sleep(2)
    future.set_result(12)


async def main():
    future = make_request()
    print("Is the future done? %s" % future.done())
    value = await future
    print("Is the future done? %s" % future.done())
    print(value)

asyncio.run(main())