from asyncio import Future


future1 = Future()

print(f"Is the future done? {future1.done()}")

# устанавливаю результат сам, и тогда фьюча станет тру.
future1.set_result(10)
print(f"Is the future done? {future1.done()}")

print(f"result: {future1.result()}")  # если не установлена переменная - вылезет эксепшн.


