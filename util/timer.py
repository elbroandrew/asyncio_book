import functools
import time
from typing import Callable, Any


def async_timed():
    def wrapper(f: Callable) -> Callable:
        @functools.wraps(f)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"Staring func {f.__name__} with args: {args}, {kwargs}")
            start = time.time()
            try:
                return await f(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"Total time: {total} seconds.")

        return wrapped
    
    return wrapper