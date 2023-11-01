import asyncio
from asyncio.exceptions import TimeoutError
from util import delay

"""
'asyncio.wait_for' func accepts task obj or coroutine.
"""

async def main():
    task1 = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(task1, timeout=1)
        print(result)
    except TimeoutError:
        print('Got a timeout!')
        print(f"Was the task cancelled? {task1.cancelled()}")

asyncio.run(main())