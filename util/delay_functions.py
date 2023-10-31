import asyncio

async def delay(seconds: int) -> int:
    print(f"Awaiting for {seconds} seconds.")
    await asyncio.sleep(seconds)
    print(f"Finished awaiting for {seconds} seconds.")
    return seconds


