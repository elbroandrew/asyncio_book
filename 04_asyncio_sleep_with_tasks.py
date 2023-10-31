# -*- coding: utf-8 -*-

import asyncio
from util import delay

"""
Creating a task is achieved by using the 'asyncio.create_task' function. When we call
this function, we give it a coroutine to run, and it returns a task object instantly. Once
we have a task object, we can put it in an await expression that will extract the return
value once it is complete.
"""


async def main():
    task_object = asyncio.create_task(delay(3))
    print(f"Type of task object is: {type(task_object)}")
    result = await task_object
    print(result)

asyncio.run(main())

