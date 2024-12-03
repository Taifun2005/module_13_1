import time
import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    max_ = power + 1
    for i in range(1,6):
        await asyncio.sleep(max_ - power)
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('djon',5))
    task2 = asyncio.create_task(start_strongman('marat',7))
    task3 = asyncio.create_task(start_strongman('djini',3))
    await task1
    await task2
    await task3

start = time.time()
asyncio.run(start_tournament())
end = time.time()

print(f'Финиш! все силачи выпольнили задание за  {end - start} время')