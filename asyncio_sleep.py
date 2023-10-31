# -*- coding: utf-8 -*-

import asyncio
from util import delay

async def add_one(n: int) -> int:
    await delay(2)
    return n + 1

async def hello_there_coro() -> str:
    await delay(1)  # await puts everyithing on pause
    return 'hello world!'

async def main():
    message = await hello_there_coro()
    print("some message.") # this will happen after we 'awaited' the result from 'hello_there' func.
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)

"""
Что тут происходит:
меседж ставит на паузу мэйн функцию, и ждет результата из hello_there ф-ии.
никакой код не выполнятеся в мэйн дальше.
внутри hello_there тоже ожидается пауза 1 сек,
затем только возвращается результат и присваивается меседжу.
далее мэйн просыпается и принтует 'some message'.
затем на add_one снова мэйн засыпает и внутри add_one тоже ожидаем результат 2 сек.
никакой код выполнить нельзя в мэйне в этот момент.
далее происходит возврат результата в переменную one_plus_one и
далее всё это принтуется one_plus_one и затем меседж.
Это и есть КООПЕРАТИВНАЯ многозадачность - где я сам указываю кому и сколько ожидать.
Следующий пример будет с тасками - обертками над корутинами - они позволяют await'у не блочить
основную ф-ию.
С await'ом мы НЕ запускаем код конкурентно, это просто корутин, из которой можно выйти и вернуться обратно,
а код все равно блокирующим остается. Для конкурентности нужны ТАСКИ, которые обрабатывает EVENT LOOP уже.
"""

asyncio.run(main())

