import requests
import asyncio

async def print_response():
    resp = requests.get("https://www.example.com")
    print(f"Response: {resp.status_code}.")


def counter(n: int) -> int:
    print(n + 1)

async def main():
    print("running coro1")
    res1 = await print_response()
    print("end running coro1")
    print("running coro2")
    res2 = await print_response()
    print("end running coro2")

asyncio.run(main())