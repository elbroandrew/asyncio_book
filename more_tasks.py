# -*- coding: utf-8 -*-


import asyncio
from util import delay

async def main():
    sleep1 = asyncio.create_task(delay(2))
    sleep2 = asyncio.create_task(delay(2))    
    sleep3 = asyncio.create_task(delay(2))

    await sleep1
    await sleep2
    await sleep3


asyncio.run(main())

"""
Т.е если бы я вызвал 'await delay(2)' без create_task, то
ожидал бы завершения ф-ии. Затем запустилась бы вторая 'await delay(2)' etc.
А так, я закинул все задачи в эвент луп и уже ожидаю все результаты на await sleep1,2,3.
"""