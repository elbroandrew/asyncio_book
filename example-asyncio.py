import time
import requests
import threading

def read_example() -> None:
    response = requests.get("https://www.example.com")
    print(f"response status code: {response.status_code}")

t1 = threading.Thread(target=read_example)
t2 = threading.Thread(target=read_example)


start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Running synchronously: {end - start:.4f} secs.")