# -*- coding: utf-8 -*-

import asyncio
from util import delay
from asyncio.exceptions import TimeoutError

'''
'asyncio.shield' позволяет корутине продолжить работу, когда сработает таймаут.
'''

async def main():
    task = asyncio.create_task(delay(3))
    try:
        result = await asyncio.wait_for(asyncio.shield(task), 1)
        print(result)
    except TimeoutError:
        print("Notification: task took longer then 1 second.")
        result = await task
        print(result)

asyncio.run(main())