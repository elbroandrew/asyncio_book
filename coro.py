import requests
import asyncio

async def print_response():
    resp = requests.get("https://www.example.com")
    print(f"Response: {resp.status_code}.")


def counter(n: int) -> int:
    print(n + 1)

async def main():
    counter(10)
    res1 = await print_response()


asyncio.run(main())