import asyncio


async def hello_there_coro() -> str:
    await asyncio.sleep(2)
    return 'hello world!'

async def main():
    message = await hello_there_coro()
    print(message)


asyncio.run(main())

