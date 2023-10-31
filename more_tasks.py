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