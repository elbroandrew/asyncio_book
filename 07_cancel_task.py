import asyncio
from util import delay
from asyncio import CancelledError

async def main():
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0
    while not long_task.done():
        print(f"Task is not finished. Checking it again in a second.")
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print("The task was cancelled.")


asyncio.run(main())